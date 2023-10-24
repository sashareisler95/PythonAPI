import json
import pytest
import requests

user_agents = {
    "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30": {
        'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
    "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1": {
        'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)": {'platform': 'Googlebot',
                                                                                 'browser': 'Unknown',
                                                                                 'device': 'Unknown'},
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0": {
        'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
    "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1": {
        'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
}


@pytest.mark.parametrize('userAgent', user_agents.keys())
def test_user_agent(userAgent):
    response = requests.get('https://playground.learnqa.ru/ajax/api/user_agent_check',
                            headers={"User-Agent": userAgent}, verify=False)
    response_json = json.loads(response.content)
    results = user_agents[userAgent]
    assert results.get('device') == response_json[
        'device'], f"Некорректный девайс! В ответе:{response_json['device']}, ожидаемый девайс: {results.get('device')}"
    assert results.get('browser') == response_json[
        'browser'], f"Некорректный браузер! В ответе:{response_json['browser']}, ожидаемый браузер: {results.get('browser')}"
    assert results.get('platform') == response_json[
        'platform'], f"Некорректная платформа! В ответе:{response_json['platform']}, ожидаемая платформа: {results.get('platform')}"

