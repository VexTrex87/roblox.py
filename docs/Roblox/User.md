# `class` roblox.**User**

## `str` roblox.User.**name**
The user's name.

## `str` roblox.User.**display_name**
The user's display name.

## `int` roblox.User.**id**
The user's unique ID.

## `str` roblox.User.**description**
The user's description.

## `bool` roblox.User.**banned**
Specifies if the user is banned.

## `datetime.datetime` roblox.User.**created**
The user's account's creation date.

## `method` roblox.User.**get_attributes()** -> `dict`
Returns the user's attributes.

## `method` roblox.User.**get_username_history(limit)** -> `list str`
Returns the user's username history. Supported limits include 10, 25, 50, and 100.

## `method` roblox.User.**get_status()** -> `str`
Returns the user's status.