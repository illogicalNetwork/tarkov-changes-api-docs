---
title: Tarkov Changes API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - python
  - javascript

toc_footers:
  - <a href=https://tarkov-changes.com/developer'>Sign Up for a Developer Key</a>

includes:
  - errors

search: true

code_clipboard: true

meta:
  - name: description
    content: Here lies the documentation for the Tarkov Changes API. A collection of resources about Escape from Tarkov.
---

# Introduction

Welcome to the Tarkov Changes API.

We have language bindings in Shell, Python, and JavaScript! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.


# Authentication

To use the API (like the website does) simply make a call to `/v1/auth` and it will return a JSON object with a key of "CSRF-Token" which contains your temporary API key.

To obtain a more permanent API key which gives you access to a higher rate limit and other features please see https://tarkov-changes.com/developer.


```python

```

```shell

```

```javascript

```

# Ammo

## Get Current Ammo 

```python
import requests

headers = { 
  "CSRF-Token": $token,
}

r = requests.get("https://api.tarkov-changes.com/v1/ammo", headers=headers)
```

```shell

```

```javascript

```

> The above command returns JSON structured like this:

```json
{
    "msg": "",
    "results": [
        ...
        {
            "Accuracy": "0",
            "Armor Damage": "26",
            "Ballistic Coefficient": "1",
            "Buckshot Count": "8",
            "Caliber": "Caliber23x75",
            "Cell Height": "1",
            "Cell Width": "1",
            "Description": null,
            "Discard Limit": "-1",
            "Durability Burn": "1",
            "Failure to Feed": "0",
            "Flesh Damage": "32",
            "Frag Chance": "0",
            "Heat Factor": "1",
            "Heavy Bleeding Delta": "0",
            "Item ID": "5f647fd3f6e4ab66c82faed6",
            "Item Weight": "0.08",
            "Light Bleeding Delta": "0",
            "Malfunction Chance": null,
            "Max Stack Size": "15",
            "Misfire Chance": "0.01",
            "Name": null,
            "Penetration Chance": "0.02",
            "Penetration Power": "3",
            "Projectile Speed": "270",
            "Recoil": "0",
            "Stamina Burn per Dmg": "0.24"
        }
    ],
    "status": "success"
}
```

This endpoint retrieves current ammo.

### HTTP Request

`GET https://api.tarkov-changes.com/v1/ammo`

# Armor

# Backpacks

# Banned

# Barters

# Boss

# Buffs

# Credits

# Clothing

# Containers

# Firearms

# Food

# Grenades

# Headphones

# Helmets

# Items

# Limits

# Karma

# Knives

# Keys

# Maps

# Magazines

# Medicals

# Mods

# Money

# Rigs

# Search

# Trader Resets

# Weather

## Get Current Weather Conditions

```python
import requests

headers = { 
  "CSRF-Token": $token,
}

r = requests.get("https://api.tarkov-changes.com/v1/weather", headers=headers)
```

```shell

```

```javascript

```

> The above command returns JSON structured like this:

```json
{
    "msg": "",
    "results": [
        {
            "cloud": -0.995,
            "date": "2022-12-28",
            "fog": 0.002,
            "pressure": 760,
            "rain": 1,
            "rain_intensity": 0.0,
            "temp": 24,
            "time": "2022-12-28 04:15:03",
            "timestamp": 1672190103,
            "wind_direction": 2,
            "wind_gustiness": 0.017,
            "wind_speed": 1
        }
    ],
    "status": "success"
}
```

This endpoint retrieves current weather conditions in Tarkov.

### HTTP Request

`GET https://api.tarkov-changes.com/v1/weather`

