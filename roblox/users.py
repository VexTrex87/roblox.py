import roblox.requests as requests
import datetime

"""
POST    /usernames/users
POST    /users
PATCH   /users/{userId}/display-names
PATCH   /users/{userId}/status
"""

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

    def get_username_history(self, limit):
        try:
            limit = int(limit)
        except ValueError:
            raise Exception('Could not convert limit to integer')

        if not limit in [10, 25, 50, 100]:
            raise Exception('Limit must be 10, 25, 50, or 100')

        username_history_url = f'https://users.roblox.com/v1/users/{self.id}/username-history?limit={limit}&sortOrder=Asc'
        username_history_data = requests.get(username_history_url)
        return [username['name'] for username in username_history_data['data']]

    def get_status(self):
        status_url = f'https://users.roblox.com/v1/users/{self.id}/status'
        status_data = requests.get(status_url)
        return status_data['status']

def search_users(keyword, limit):
    try:
        limit = int(limit)
    except ValueError:
        raise Exception('Could not convert limit to integer')

    if not limit in [10, 25, 50, 100]:
        raise Exception('Limit must be 10, 25, 50, or 100')
        
    url = f'https://users.roblox.com/v1/users/search?keyword={keyword}&limit={limit}'
    data = requests.get(url)
    
    users = []
    for user_data in data['data']:
        user = get_user(user_data['id'])
        users.append(user)
    return users
    
def get_user(user_id=None, username=None):
    if not user_id and not username:
        raise Exception('Missing argument: user_id or username')
    elif user_id:
        pass
    elif username:
        for user in search_users(username, limit=100):
            if user.name == username:
                return user
        else:
            return None

    url = f'https://users.roblox.com/v1/users/{user_id}'
    data = requests.get(url)
    user = User(data)
    return user
