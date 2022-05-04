import json
from secrets import blizzard_client_secret, blizzard_client_id
import requests


class Access:
    def __init__(self):
        self.token = get_access_token()

    def get_auctions(self):
        # Returns a list of auctions
        # example:
        # [{
        #   'id': 1634394199,
        #   'item': {
        #       'id': 40302,
        #       'modifiers': [
        #           {
        #               'type': 28,
        #               'value': 1017
        #            }
        #         ]
        #     },
        #     'buyout': 9005800,
        #     'quantity': 1,
        #     'time_left': 'SHORT'
        # }]
        headers = {
            'Authorization': f'Bearer {self.token}',
        }
        params = {
            'namespace': 'dynamic-us',
            'locale': 'en_US',
        }
        response = requests.get(
            'https://us.api.blizzard.com/data/wow/connected-realm/3209/auctions',
            headers=headers,
            params=params,
        )
        dict_response = json.loads(response.content)
        auction_list = dict_response['auctions']
        return auction_list


def get_access_token():
    response = requests.post(
        'https://us.battle.net/oauth/token',
        data={'grant_type': 'client_credentials'},
        auth=(blizzard_client_id, blizzard_client_secret),
    )
    response_bytes = response.content
    response_dict = json.loads(response_bytes)
    return response_dict['access_token']
