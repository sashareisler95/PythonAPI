import requests

payload = {"name": "User"}
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload, verify=False)
print(response.text)
