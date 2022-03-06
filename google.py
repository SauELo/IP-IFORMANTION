import requests, json
try:
    while True:
        j2 = input('Write a IP or write "exit" for exit: ')
        if j2 != "exit":
            req = requests.get(f'https://ipinfo.io/{j2}/geo')
            j3 = json.loads(req.text)
            print()
            print(f'The IP is located at:\nCountry: {j3["country"]}\nRegion: {j3["region"]}\nCity: {j3["city"]}\nPostal: {j3["postal"]}\nORG: {j3["org"]}\nLocalization: {j3["loc"]}\nTimeZone: {j3["timezone"]}')
            print()
        if j2 == "exit":
            break
            exit()
except:
    print('Error')
