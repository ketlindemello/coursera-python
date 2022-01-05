import requests
import json

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json'
else:
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json'


while True:
    address = input('Enter location: ')
    if len(address) < 1: break


    payload = dict()
    payload['address'] = address
    print(payload)

    if api_key is not False: payload['key'] = api_key
    print(payload)

    r = requests.get(serviceurl, params=payload)

    print('Retrieved', r.url)

    data = r.text
   
    print('Retrived', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to retrieve')
        print(data)

        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print('lat', lat, 'lng', lng)

    location = js['results'][0]['formatted_address']
    print(location)
    
    
