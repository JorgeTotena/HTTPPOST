import requests
from datetime import datetime
TOKEN = "122345678Ab."
USERNAME = "jorget123"
GRAPH = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

"""user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text) """ #CREATE AN ACCOUNT

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Math Graph",
    "unit": "minutes",
    "type": "int",
    "color": "kuro",
    "timezone": "America/Bogota"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

"""r2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(r2.text) """ #CREATE A GRAPH

today = datetime.now()
#datetime(year=2025, month=2, day=28)
date_formatted = today.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes of Math did you study today: "),

}
#ADD A NEW PIXEL
#r3 = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#print(r3.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date_formatted}"
update_pixel_config = {
    "quantity": "50",

}

#UPDATE A PIXEL
#r4 = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
#print(r4.text)
#print(r4.status_code)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date_formatted}"

# DELETE A PIXEL
# r5 = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(r5.text)
# print(r5.status_code)

