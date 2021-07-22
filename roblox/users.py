import roblox.requests as requests
import datetime

class User():
    def __init__(self, info):
        self.name = info.get('name')
        self.display_name = info.get('displayName') or None
        self.id = info.get('id')
        self.description = info.get('description') or ''
        self.banned = info.get('isBanned') or False
        self.created = info.get('created') and datetime.datetime.strptime(info['created'], '%Y-%m-%dT%H:%M:%S.%fZ')

    def get_attributes(self):
        return {
            'name': self.name,
            'display_name': self.display_name,
            'id': self.id,
            'description': self.description,
            'banned': self.banned,
            'created': self.created,
        }

def get_user(user_id):
    url = f'https://users.roblox.com/v1/users/{user_id}'
    data = requests.get(url)
    user = User(data)
    return user