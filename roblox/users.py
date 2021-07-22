import roblox.exception as RobloxException
import requests
import datetime

class BaseUser():
    def _get_user_info(self, user_id):
        try:
            user_id = int(user_id)
        except:
            raise RobloxException.InvalidArgument('Could not convert user_id to integer')

        if user_id <= 0:
            raise RobloxException.InvalidArgument('user_id must be greater than 0')

        url = f'https://users.roblox.com/v1/users/{user_id}'
        r = requests.get(url)
        
        if r.status_code == 200:
            return r.json()
        else:
            if r.status_code == 404:
                raise RobloxException.NotFound(f'[{r.status_code}] {r.reason}')
            else:
                raise RobloxException.UnknownError(f'[{r.status_code}] {r.reason}')

    def _get_user_status(self, user_id):
        try:
            user_id = int(user_id)
        except:
            raise RobloxException.InvalidArgument('Could not convert user_id to integer')

        url = f'https://users.roblox.com/v1/users/{user_id}/status'
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()
        else:
            if r.status_code == 400:
                raise RobloxException.BadRequest(f'[{r.status_code}] {r.reason}')
            elif r.status_code == 429:
                raise RobloxException.TooManyRequests(f'[{r.status_code}] {r.reason}')
            else:
                raise RobloxException.UnknownError(f'[{r.status_code}] {r.reason}')

    def _get_user_username_history(self, user_id, limit):
        try:
            user_id = int(user_id)
        except:
            raise RobloxException.InvalidArgument('Could not convert user_id to integer')
        
        try:
            limit = int(limit)
        except:
            raise RobloxException.InvalidArgument('Could not convert limit to integer')

        if not limit in [10, 25, 50, 100]:
            raise RobloxException.InvalidArgument('Limit must be 10, 25, 50, or 100')

        url = f'https://users.roblox.com/v1/users/{user_id}/username-history?limit={limit}&sortOrder=Asc'
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()
        else:
            if r.status_code == 400:
                raise RobloxException.BadRequest(f'[{r.status_code}] {r.reason}')
            elif r.status_code == 429:
                raise RobloxException.TooManyRequests(f'[{r.status_code}] {r.reason}')
            else:
                raise RobloxException.UnknownError(f'[{r.status_code}] {r.reason}')

    def _search_users(self, keyword, limit):
        try:
            keyword = str(keyword)
        except:
            raise RobloxException.InvalidArgument('Could not convert keyword to string')

        if len(keyword) < 3 or len(keyword) > 20:
            raise RobloxException.InvalidArgument('keyword must be between 3 and 20 characters')

        try:
            limit = int(limit)
        except:
            raise RobloxException.InvalidArgument('Could not convert limit to integer')

        if not limit in [10, 25, 50, 100]:
            raise RobloxException.InvalidArgument('Limit must be 10, 25, 50, or 100')

        url = f'https://users.roblox.com/v1/users/search?keyword={keyword}&limit={limit}'
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()
        else:
            if r.status_code == 400:
                raise RobloxException.BadRequest(f'[{r.status_code}] {r.reason}')
            elif r.status_code == 429:
                raise RobloxException.TooManyRequests(f'[{r.status_code}] {r.reason}')
            else:
                raise RobloxException.UnknownError(f'[{r.status_code}] {r.reason}')

class User(BaseUser):
    def __init__(self, info):
        self._name = info.get('name')
        self._display_name = info.get('displayName') or None
        self._id = info.get('id')
        self._description = info.get('description') or ''
        self._banned = info.get('isBanned') or False
        self._created = info.get('created') and datetime.datetime.strptime(info['created'], '%Y-%m-%dT%H:%M:%S.%fZ') or None

    @property
    def name(self):
        return self._name

    @property
    def display_name(self):
        return self._display_name

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def banned(self):
        return self._banned

    @property
    def created(self):
        return self._created

    def get_status(self):
        data = self._get_user_status(self.id)
        return data['status']

    def get_username_history(self, limit):
        data = self._get_user_username_history(self.id, limit)
        return [username['name'] for username in data['data']]

def search_users(keyword, limit):
    data = BaseUser()._search_users(keyword, limit)

    users = []
    for user_data in data['data']:
        user = get_user(user_data['id'])
        users.append(user)
    return users

def get_user(user_id=None, username=None):
    if not user_id and not username:
        raise RobloxException.MissingArgument('Missing argument: user_id or username')
    elif user_id:
        pass
    elif username:
        for user in search_users(username, limit=100):
            if user.name == username:
                return user
        else:
            return None

    data = BaseUser()._get_user_info(user_id)
    user = User(data)
    return user
