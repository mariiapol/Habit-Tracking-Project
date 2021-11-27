import requests
from datetime import datetime

TOKEN = "your token"
USERNAME = "your userneme"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


graf_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graf_config = {
    "id": "graph1",
    "name": "Python Graph",
    "unit": "hour",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

add_pixel_endpoint = "https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
add_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? ")
}

response = requests.post(url=add_pixel_endpoint, json=add_params, headers=headers)
print(response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20210325"

param = {
    "quantity": "1"
}

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20210325"











