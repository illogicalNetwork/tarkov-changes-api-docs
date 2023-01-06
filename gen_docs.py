import os
import traceback

import requests
import json
from genson import SchemaBuilder

API_URL = os.environ.get("API_URL", "https://api.tarkov-changes.com/v1")
AUTH_HEADER = {
    "AUTH-Token": "2aa18cb07fecec4b7923"
  }
ENDPOINTS = requests.get(f"{API_URL}/endpoints", headers=AUTH_HEADER).json().get("Endpoint List")
TITLE = "Tarkov Changes API Reference"

doc_markdown = f"""---
title: {TITLE}

language_tabs:
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

Welcome to the documentation about the Tarkov Changes API.

We have language bindings in Shell, Python, and JavaScript! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.


# Authentication

To use the API please see https://tarkov-changes.com/developer. Once connected, you will set the "AUTH-Token" header as part of every API request.

"""

for endpoint in ENDPOINTS:
  builder = SchemaBuilder()
  schema = builder.add_object(requests.get(f"{API_URL}/{endpoint.lower()}", headers=AUTH_HEADER).json())
  doc_markdown += f"""# {endpoint}

## Get (all) {endpoint}

```python
import requests
import json

url = "{API_URL}/{endpoint}"
headers = {{
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "{API_URL}/{endpoint.lower()}" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {{
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
}};

fetch("{API_URL}/{endpoint}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{builder.to_json(indent=2)}
```

### HTTP Request

`GET https://{API_URL}/{endpoint.lower()}`

## Get a specific {endpoint}

```python
import requests
import json

url = "{API_URL}/{endpoint}?query=foo"
headers = {{
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "{API_URL}/{endpoint.lower()}?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {{
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
}};

fetch("{API_URL}/{endpoint}?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{builder.to_json(indent=2)}
```

### HTTP Request

`GET https://{API_URL}/{endpoint.lower()}?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

"""

# Search
builder = SchemaBuilder()
schema = builder.add_object(requests.get(f"{API_URL}/search?query=killa", headers=AUTH_HEADER).json())
endpoint = "search"
doc_markdown += f"""
# Search

## Search for a specific item

```python
import requests
import json

url = "{API_URL}/{endpoint}?query=foo"
headers = {{
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "{API_URL}/{endpoint.lower()}?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {{
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
}};

fetch("{API_URL}/{endpoint}?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{builder.to_json(indent=2)}
```

### HTTP Request

`GET {API_URL}/search?query=killa`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

"""

# Weather
builder = SchemaBuilder()
schema = builder.add_object(requests.get(f"{API_URL}/weather", headers=AUTH_HEADER).json())
endpoint = "weather"
doc_markdown += f"""
# Weather

## Get up to date weather information

```python
import requests
import json

url = "{API_URL}/{endpoint}"
headers = {{
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "{API_URL}/{endpoint.lower()}" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {{
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
}};

fetch("{API_URL}/{endpoint}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{builder.to_json(indent=2)}
```

### HTTP Request

`GET {API_URL}/{endpoint}`

"""
print (doc_markdown)



