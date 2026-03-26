import requests

url = "http://127.0.0.1:5000/event"

normal_player = {
    "user_id": "player1",
    "speed": 50,
    "actions_per_sec": 5
}

cheater = {
    "user_id": "hacker99",
    "speed": 200,
    "actions_per_sec": 40
}

normal_response = requests.post(url, json=normal_player)
cheater_response = requests.post(url, json=cheater)

print("Normal Player:", normal_response.status_code, normal_response.json())
print("Cheater:", cheater_response.status_code, cheater_response.json())
