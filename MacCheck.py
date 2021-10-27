import requests
import json
import crayons


# Fetching the all Apple Stores in Germany for my MBP Config
responseOld = requests.get(
    "https://www.apple.com/de-edu/shop/fulfillment-messages?parts.0=MKGP3D%2FA&searchNearby=true&mt=regular&store=R331&_=1635346957941")


response = requests.get(
    "https://www.apple.com/de-edu/shop/fulfillment-messages?parts.0=MK1A3D%2FA&searchNearby=true&mt=regular&store=R331&_=1635346957951")
jsonData = response.json()


# Checking the fetched Apple Stores for Pickup Availability
for store in jsonData['body']['content']['pickupMessage']['stores']:
    availabilityText = store['partsAvailability']['MK1A3D/A']['pickupDisplay']
    available = True if availabilityText == "available" else False
    print("{}: {}".format(store['storeName'],
          crayons.green('✔ Verfügbar') if available else crayons.red('Nicht Verfügbar ✖')))
