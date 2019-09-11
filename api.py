import requests

root_url = "https://goldennumber.aiedu.msra.cn"

def new_user(nick_name: str) -> bool:
    api_url = "/api/NewUser"
    parameter = {}
    parameter["nickName"] = nick_name
    response = requests.get(root_url + api_url, params=parameter)
    status_code = response.status_code
    return 200 <= response < 300

