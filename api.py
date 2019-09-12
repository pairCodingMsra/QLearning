import requests

root_url = "https://goldennumber.aiedu.msra.cn"


def new_user(nick_name: str) -> "{userId, nickName} / None":
    api_url = "/api/NewUser"
    parameter = {"nickName": nick_name}
    response = requests.get(root_url + api_url, params=parameter)
    status_code = response.status_code
    if 200 <= status_code < 300:
        return response.json()
    else:
        return None


def nick_name(user_id: str, nick_name: str) -> "{userId, nickName} / None":
    api_url = "/api/NickName"
    data = {"userId": user_id, "nickName": nick_name}
    response = requests.post(root_url + api_url, data=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return None


def new_room(numbers: int, duration: int, user_id: str, user_count: int, round_count: int,
             manual: bool) -> "{roomId} / None":
    api_url = "/api/NewRoom"
    data = {"numbers": numbers, "duration": duration, "uid": user_id, "userCount": user_count,
            "roundCount": round_count, "manuallyStart": 1 if manual else 0}
    response = requests.get(root_url + api_url, params=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return None


def start_game(user_id: str, room_id: int) -> "success / None":
    api_url = "/api/NewRoom"
    data = {"uid": user_id, "roomid": room_id}
    response = requests.get(root_url + api_url, params=data)
    if 200 <= response.status_code < 300:
        return "success"
    else:
        return None

def state(user_id: str, room_id: int):
    """
    -> "{\
      roundId: string,\
      leftTime: 0,\
      roundEndTime: 2019-09-12T07:13:04.160Z,
      userId: string,
      nickName: string,
      roomId: 0,
      numbers: 0,
      duration: 0,
      state: 0,
      hasSubmitted: true,
      isRoomCreator: true,
      maxUserCount: 0,
      currentUserCount: 0,
      totalRoundCount: 0,
      finishedRoundCount: 0
    } / None"v
    """
    api_url = "/api/State"
    data = {"uid": user_id, "roomid": room_id}
    response = requests.get(root_url + api_url, params=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return None


def submit(numbers: int, duration: int, user_id: str, user_count: int, round_count: int,
             manual: bool) -> "{roomId} / None":
    api_url = "/api/NewRoom"
    data = {"numbers": numbers, "duration": duration, "uid": user_id, "userCount": user_count,
            "roundCount": round_count, "manuallyStart": 1 if manual else 0}
    response = requests.get(root_url + api_url, params=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return None


def new_room(numbers: int, duration: int, user_id: str, user_count: int, round_count: int,
             manual: bool) -> "{roomId} / None":
    api_url = "/api/NewRoom"
    data = {"numbers": numbers, "duration": duration, "uid": user_id, "userCount": user_count,
            "roundCount": round_count, "manuallyStart": 1 if manual else 0}
    response = requests.get(root_url + api_url, params=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return None


def new_room(numbers: int, duration: int, user_id: str, user_count: int, round_count: int,
             manual: bool) -> "{roomId} / None":
    api_url = "/api/NewRoom"
    data = {"numbers": numbers, "duration": duration, "uid": user_id, "userCount": user_count,
            "roundCount": round_count, "manuallyStart": 1 if manual else 0}
    response = requests.get(root_url + api_url, params=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return None
