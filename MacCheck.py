import requests
import json
import crayons

import Constants

bot = Constants.CHATBOT_TOKEN
chat_id = Constants.CHATBOT_CHATID

# internal apple code for my config
mbp16 = "MK1A3D/A"

# URL for sending the Message via Telegram
telegramUrl = "https://api.telegram.org/bot{}/sendMessage".format(bot)

# Fetching the all Apple Stores in Germany for my MBP Config


response = requests.get(
    "https://www.apple.com/de-edu/shop/fulfillment-messages?parts.0=MK1A3D%2FA&searchNearby=true&mt=regular&store=R331&_=1635346957951")

jsonData = response.json()


# Checking the fetched Apple Stores for Pickup Availability
for store in jsonData['body']['content']['pickupMessage']['stores']:
    availabilityText = store['partsAvailability'][mbp16]['pickupDisplay']

    available = True if availabilityText == "available" else False

    print("{}: {}".format(store['storeName'],
          crayons.green('✔ Verfügbar') if available else crayons.red('Nicht Verfügbar ✖')))

    # If my MacBook is available, the Telegram bot sends me a message with the Store Name
    if available:
        message = requests.post(telegramUrl, params={
            "chat_id": chat_id, "text": "Dein Macbook ist verfügbar im Apple Store {}!".format(store['storeName'])})
        print(message)
