import roblox.requests as requests
import datetime

"""
GET     /users/search
PATCH   /users/{userId}/display-names
POST    /usernames/users
POST    /users
PATCH   /users/{userId}/status
"""

class User():
    def __init__(self, info):
        self.name = info.get('name')
        self.display_name = info.get('displayName') or None
        self.username_history = info.get('username_history') or []
        self.id = info.get('id')
        self.description = info.get('description') or ''
        self.status = info.get('status') or ''
        self.banned = info.get('isBanned') or False
        self.created = info.get('created') and datetime.datetime.strptime(info['created'], '%Y-%m-%dT%H:%M:%S.%fZ')

    def get_attributes(self):
        return {
            'name': self.name,
            'display_name': self.display_name,
            'username_history': self.username_history,
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'banned': self.banned,
            'created': self.created,
        }

def get_user(user_id):
    url = f'https://users.roblox.com/v1/users/{user_id}'
    data = requests.get(url)

    status_url = f'https://users.roblox.com/v1/users/{user_id}/status'
    status_data = requests.get(status_url)
    data['status'] = status_data['status']

    username_history_url = f'https://users.roblox.com/v1/users/{user_id}/username-history?limit=100&sortOrder=Asc'
    username_history_data = requests.get(username_history_url)
    data['username_history'] = [username['name'] for username in username_history_data['data']]

    user = User(data)
    return user

def search_users(keyword, limit=100):
    if not limit:
        limit = 100

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