import time


class Token:
    def __init__(self, access_token):
        self.access_token = access_token
        self.expiration = time.time() + (24*60*59)

    def is_valid(self):
        return time.time() < self.expiration
