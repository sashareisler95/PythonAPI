import json
import time
import requests

response_first = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", verify=False)
token = "token=" + str(json.loads(response_first.content)['token'])
seconds = json.loads(response_first.content)['seconds']
response_status = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", verify=False, params=token)
time.sleep(seconds)
response_result = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", verify=False, params=token)


print(response_status.text)
print(response_result.text)
