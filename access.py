import json
from secrets import blizzard_client_secret, blizzard_client_id
import requests
import pickle
import time


class Access:
    def __init__(self):
        self.token = None
        try:
            with open('token.pickle', 'rb') as f:
                self.token = pickle.load(f)
        except FileNotFoundError:
            self.token = self.get_access_token()

    def __del__(self):
        with open('token.pickle', 'wb') as f:
            pickle.dump(self.token, f)

    def get_auctions(self):
        headers = {
            'Authorization': f'Bearer {self.get_access_token().access_token}',
        }
        params = {
            'namespace': 'dynamic-us',
            'locale': 'en_US',
        }
        print('Requesting auctions.')
        response = requests.get(
            'https://us.api.blizzard.com/data/wow/connected-realm/3209/auctions',
            headers=headers,
            params=params,
        )
        dict_response = json.loads(response.content)
        auction_list = dict_response['auctions']
        return auction_list

    def get_access_token(self):
        if self.token is not None:
            if self.token.is_valid():
                return self.token
        print('Requesting access token.')
        response = requests.post(
            'https://us.battle.net/oauth/token',
            data={'grant_type': 'client_credentials'},
            auth=(blizzard_client_id, blizzard_client_secret),
        )
        response_dict = json.loads(response.text)
        self.token = Token(response_dict['access_token'])
        return self.token


class Token:
    def __init__(self, access_token):
        self.access_token = access_token
        self.expiration = time.time() + (24*60*59)

    def is_valid(self):
        return time.time() < self.expiration