import requests


def check_compare_query_type(method_type, method=''):
    if method == '':
        match method_type:
            case 'get':
                response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", verify=False)
            case 'post':
                response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", verify=False)
            case 'put':
                response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", verify=False)
            case 'delete':
                response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", verify=False)
            case 'head':
                response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", verify=False)
    else:
        match method_type:
            case 'get':
                response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method, verify=False)
            case 'post':
                response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            case 'put':
                response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            case 'delete':
                response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            case 'head':
                response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
    return response


response1 = check_compare_query_type('post')
response2 = check_compare_query_type('head')
response3 = check_compare_query_type('get', 'method=GET')

print(f"Запрос без параметра - Статус-код {response1.status_code} - {response1.text}")
print(f"Запрос не из списка без параметра - Статус-код {response2.status_code}")
print(f"Запрос из списка с параметром - Статус-код {response3.status_code} - {response3.text}")

methods = ('method=GET', 'method=POST', 'method=PUT', 'method=DELETE')
request_types = ('get', 'post', 'put', 'delete')
fail_cases = []
for request_type in request_types:
    for method in methods:
        request = check_compare_query_type(request_type, method)
        if request.status_code == 200 and request_type not in method.lower() and request.text == '{"success":"!"}':
            fail_case = str("request_type=" + request_type) + ' ' + str(method)
            fail_cases.append(fail_case)
        if request.status_code != 200 and request_type in method.lower():
            fail_case = str("request_type=" + request_type) + ' ' + str(method)
            fail_cases.append(fail_case)


print(f"Проблемные кейсы по сочетанию типа запроса и метода - {fail_cases}")
