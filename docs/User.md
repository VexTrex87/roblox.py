# `class` **roblox**

## `method` roblox.**get_user(user_id)** -> `roblox.User`
Returns the roblox user.

## `method` roblox.**search_users(keyword, limit=None)** -> `list roblox.User`
Returns users with usernames similar to the keyword. If there is no limit, the limit will be set to the maximum limit. The maximum limit is 100 and the minimum limit is 1.

# `class` roblox.**User**

## `str` roblox.User.**name**
The user's name.

## `str` roblox.User.**display_name**
The user's display name.

## `str` roblox.User.**username_history**
The user's username history.

## `int` roblox.User.**id**
The user's unique ID.

## `str` roblox.User.**description**
The user's description.

## `str` roblox.User.**status**
The user's status.

## `bool` roblox.User.**banned**
Specifies if the user is banned.

## `datetime.datetime` roblox.User.**created**
The user's account's creation date.

## `method` roblox.User.**get_attributes()** -> `dict`
Returns the user's attributes.