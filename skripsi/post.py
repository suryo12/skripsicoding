import requests
import json
import time, datetime

server_domain = 'http://localhost:8000/'
app = 'landslide/api/'


def post_data():
    url = server_domain + app
    headers = {'content-type': 'application/json'}
    data = {"node_name" : "Magelang1",
            "location" : "Magelang Km 10",
            "timestamp" : datetime.datetime.now().isoformat(),
            "vibration": "56",
            "coordinate_x" : "45",
            "coordinate_x" : "11",
            "coordinate_x" : "78"
          }
            response = requests.post(url, data=json.dumps(data), headers =headers)

    if response.status_code != 201:
        print('Error: {}'.format(response.text))
    else:
        print('Created: {}'.format(json.loads(response.text)))


if __name__ == '__main__':
    post_data()
