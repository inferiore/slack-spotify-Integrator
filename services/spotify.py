import requests
from requests import HTTPError
import base64
from services.common import config
import json

class Spotify:

    def __init__(self):
        self.access_token = None
        self.refresh_token = None

    def getToken(self, code):
        self.access_token = None
        self.refresh_token = None

        app_token = (config()["client_id"]+":"+config()["client_secret"])
        headers = {'Authorization': "Basic "+str(base64.b64encode(app_token.encode("utf-8")),"utf-8"),
                   "Content-Type": "application/x-www-form-urlencoded"}
        payload = ({'grant_type': "authorization_code",
                              "code": code,
                              "redirect_uri": config()["public_url"]})
        response = requests.post(config()["endpoints"]["login"],data=payload,headers=headers)

        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
            self.refresh_token = response.json()["refresh_token"]

    def refreshToken(self):
        self.access_token = None
        app_token = (config()["client_id"] + ":" + config()["client_secret"])
        headers = {'Authorization': "Basic " + str(base64.b64encode(app_token.encode("utf-8")), "utf-8"),
                   "Content-Type": "application/x-www-form-urlencoded"}
        payload = ({'grant_type': "refresh_token",
                    "refresh_token": self.refresh_token})
        response = requests.post(config()["endpoints"]["login"], data=payload, headers=headers)

        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
            print("new token",self.access_token)
    def pause(self):
        try:
            payload = json.dumps({'device_id': config()["device_id"]})
            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       'Authorization': "Bearer " + self.access_token}
            request = requests.put(config()["endpoints"]["pause"],data=(payload), headers=headers)
            if(request.status_code != "200"):
                print(request.content)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6

        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6

    def play(self):
        try:
            payload = json.dumps({'device_id': config()["device_id"]})

            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       'Authorization': "Bearer " + self.access_token}
            request = requests.put(config()["endpoints"]["play"],data=(payload), headers=headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6

        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6


