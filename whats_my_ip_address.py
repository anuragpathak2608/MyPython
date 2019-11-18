import requests
import json

result = requests.get('https://helloacm.com/api/what-is-my-ip-address/')
result1 = "your ip {} is your public address: ".format(result.text)
print(result1)