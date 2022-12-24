import requests

request = requests.get('https://www.google.com')

if request.status_code == 200:
    print(request.status_code)
else:
    print('There seems to be an error connecting to the domain. This is the errror received: ' + request.status_code)



