import os
import requests
import json
from genson import SchemaBuilder

API_URL = "https://api.tarkov-changes.com/v1"
TITLE = "Tarkov Changes API Reference"
SUPPORTED_LANGUAGES = [
  "shell",
  "python",
  "javascript"
]

ENDPOINTS = [
  "Armor",
  "Backpacks",
  "Banned",
  "Barters",
  "Boss",
  "Buffs",
  "Credits",
  "Clothing",
  "Containers",
  "Firearms",
  "Food",
  "Grenades",
  "Headphones",
  "Helmets",
  "Items",
  "Limits",
  "Karma",
  "Knives",
  "Keys",
  "Maps",
  "Magazines",
  "Medicals",
  "Mods",
  "Money",
  "Rigs",
  "Search",
  "Trader Resets",
  "Weather",
]


doc_markdown = f"""---
title: {TITLE}

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
import requests

auth_token = requests.get("{API_URL}/auth").json().get("CSRF-Token")
```

```shell
curl "{API_URL}/auth"
```

```javascript
```

"""

for endpoint in ENDPOINTS:

  builder = SchemaBuilder()

  builder.to_schema()
  # Get the actual data
  headers = {
    "AUTH-Token": "2aa18cb07fecec4b7923"
  }

  schema = builder.add_object(requests.get(f"{API_URL}/{endpoint.lower()}", headers=headers).json())
  doc_markdown += f"""# {endpoint}

## Get All {endpoint}

```python
import requests

headers = {{ "CSRF-Token": auth_token }}

auth_token = requests.get("{API_URL}/{endpoint.lower()}", headers=headers)
```

```shell
curl "{API_URL}/{endpoint.lower()}" -H "CSRF-Token: $sometoken"
```

```javascript
```

> The above command returns the following structure:

```json
{builder.to_json(indent=2)}
```

### HTTP Request

`GET https://{API_URL}/{endpoint.lower()}`

## Get a specific {endpoint}

```python
```

```shell
```

```javascript
```

> The above command returns the following structure:

```json
```

### HTTP Request

`GET https://{API_URL}/{endpoint.lower()}?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
"""

print (doc_markdown)


