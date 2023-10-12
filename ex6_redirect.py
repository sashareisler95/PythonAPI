import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect')
print(response.text)
redirects_count = len(response.history)
end_url = response.url
print(f"Кол-во редиректов - {redirects_count}")
print(f"Конечный url - {end_url}")
