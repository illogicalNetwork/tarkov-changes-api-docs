---
title: Tarkov Changes API Reference

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

# ammo

## Get (all) ammo

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/ammo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/ammo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/ammo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Caliber": {
            "type": "string"
          },
          "Flesh Damage": {
            "type": "string"
          },
          "Penetration Power": {
            "type": "string"
          },
          "Armor Damage": {
            "type": "string"
          },
          "Accuracy": {
            "type": "string"
          },
          "Recoil": {
            "type": "string"
          },
          "Frag Chance": {
            "type": "string"
          },
          "Durability Burn": {
            "type": "string"
          },
          "Stamina Burn per Dmg": {
            "type": "string"
          },
          "Heat Factor": {
            "type": "string"
          },
          "Buckshot Count": {
            "type": "string"
          },
          "Failure to Feed": {
            "type": "string"
          },
          "Projectile Speed": {
            "type": "string"
          },
          "Misfire Chance": {
            "type": "string"
          },
          "Penetration Chance": {
            "type": "string"
          },
          "Heavy Bleeding Delta": {
            "type": "string"
          },
          "Light Bleeding Delta": {
            "type": "string"
          },
          "Ballistic Coefficient": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Accuracy",
          "Armor Damage",
          "Ballistic Coefficient",
          "Buckshot Count",
          "Caliber",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Durability Burn",
          "Failure to Feed",
          "Flesh Damage",
          "Frag Chance",
          "Heat Factor",
          "Heavy Bleeding Delta",
          "Item ID",
          "Item Weight",
          "Light Bleeding Delta",
          "Max Stack Size",
          "Misfire Chance",
          "Name",
          "Penetration Chance",
          "Penetration Power",
          "Projectile Speed",
          "Recoil",
          "Stamina Burn per Dmg"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/ammo`

## Get a specific ammo

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/ammo?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/ammo?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/ammo?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Caliber": {
            "type": "string"
          },
          "Flesh Damage": {
            "type": "string"
          },
          "Penetration Power": {
            "type": "string"
          },
          "Armor Damage": {
            "type": "string"
          },
          "Accuracy": {
            "type": "string"
          },
          "Recoil": {
            "type": "string"
          },
          "Frag Chance": {
            "type": "string"
          },
          "Durability Burn": {
            "type": "string"
          },
          "Stamina Burn per Dmg": {
            "type": "string"
          },
          "Heat Factor": {
            "type": "string"
          },
          "Buckshot Count": {
            "type": "string"
          },
          "Failure to Feed": {
            "type": "string"
          },
          "Projectile Speed": {
            "type": "string"
          },
          "Misfire Chance": {
            "type": "string"
          },
          "Penetration Chance": {
            "type": "string"
          },
          "Heavy Bleeding Delta": {
            "type": "string"
          },
          "Light Bleeding Delta": {
            "type": "string"
          },
          "Ballistic Coefficient": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Accuracy",
          "Armor Damage",
          "Ballistic Coefficient",
          "Buckshot Count",
          "Caliber",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Durability Burn",
          "Failure to Feed",
          "Flesh Damage",
          "Frag Chance",
          "Heat Factor",
          "Heavy Bleeding Delta",
          "Item ID",
          "Item Weight",
          "Light Bleeding Delta",
          "Max Stack Size",
          "Misfire Chance",
          "Name",
          "Penetration Chance",
          "Penetration Power",
          "Projectile Speed",
          "Recoil",
          "Stamina Burn per Dmg"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/ammo?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# armor

## Get (all) armor

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/armor"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/armor" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/armor", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Armor Class": {
            "type": "string"
          },
          "Armor Type": {
            "type": "string"
          },
          "Materials": {
            "type": "string"
          },
          "Protection Zones": {
            "type": "string"
          },
          "Max Durability": {
            "type": "string"
          },
          "Effective Durability": {
            "type": "number"
          },
          "Movement Speed Penalty": {
            "type": "string"
          },
          "Turn Speed Penalty": {
            "type": "string"
          },
          "Ergonomics Penalty": {
            "type": "string"
          },
          "Blunt Throughput": {
            "type": "string"
          },
          "Repair Cost": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Armor Class",
          "Armor Type",
          "Blunt Throughput",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Effective Durability",
          "Ergonomics Penalty",
          "Item ID",
          "Item Weight",
          "Materials",
          "Max Durability",
          "Max Stack Size",
          "Movement Speed Penalty",
          "Name",
          "Protection Zones",
          "Repair Cost",
          "Turn Speed Penalty"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/armor`

## Get a specific armor

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/armor?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/armor?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/armor?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Armor Class": {
            "type": "string"
          },
          "Armor Type": {
            "type": "string"
          },
          "Materials": {
            "type": "string"
          },
          "Protection Zones": {
            "type": "string"
          },
          "Max Durability": {
            "type": "string"
          },
          "Effective Durability": {
            "type": "number"
          },
          "Movement Speed Penalty": {
            "type": "string"
          },
          "Turn Speed Penalty": {
            "type": "string"
          },
          "Ergonomics Penalty": {
            "type": "string"
          },
          "Blunt Throughput": {
            "type": "string"
          },
          "Repair Cost": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Armor Class",
          "Armor Type",
          "Blunt Throughput",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Effective Durability",
          "Ergonomics Penalty",
          "Item ID",
          "Item Weight",
          "Materials",
          "Max Durability",
          "Max Stack Size",
          "Movement Speed Penalty",
          "Name",
          "Protection Zones",
          "Repair Cost",
          "Turn Speed Penalty"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/armor?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# backpacks

## Get (all) backpacks

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/backpacks"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/backpacks" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/backpacks", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Blocks Armored Vest": {
            "type": "string"
          },
          "Speed Penalty (%)": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Blocks Armored Vest",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Speed Penalty (%)"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/backpacks`

## Get a specific backpacks

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/backpacks?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/backpacks?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/backpacks?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Blocks Armored Vest": {
            "type": "string"
          },
          "Speed Penalty (%)": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Blocks Armored Vest",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Speed Penalty (%)"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/backpacks?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# banned

## Get (all) banned

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/banned"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/banned" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/banned", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Can Sell On Flea": {
            "type": "string"
          }
        },
        "required": [
          "Can Sell On Flea",
          "Name"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/banned`

## Get a specific banned

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/banned?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/banned?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/banned?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Can Sell On Flea": {
            "type": "string"
          }
        },
        "required": [
          "Can Sell On Flea",
          "Name"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/banned?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# barters

## Get (all) barters

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/barters"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/barters" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/barters", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Examine EXP": {
            "type": "string"
          },
          "Quest Only Item": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Examine EXP",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Quest Only Item"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/barters`

## Get a specific barters

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/barters?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/barters?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/barters?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Examine EXP": {
            "type": "string"
          },
          "Quest Only Item": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Examine EXP",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Quest Only Item"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/barters?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# buffs

## Get (all) buffs

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/buffs"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/buffs" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/buffs", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Buffs": {
            "type": "object",
            "properties": {
              "BuffsSJ1TGLabs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsSJ6TGLabs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsPropital": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsZagustin": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffseTGchange": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsAdrenaline": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsGoldenStarBalm": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_aquamari": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_maxenergy": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_milk": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_tarcola": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_hotrod": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_juice_army": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_water": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_borodinskiye": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_condensed_milk": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_emelya": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_mayonez": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_mre": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_sugar": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_vodka": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_jack": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_moonshine": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_purewater": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_3bTG": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_AHF1M": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_L1": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_MULE": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Meldonin": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Obdolbos": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "number"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_P22": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_KultistsToxin": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_BodyTemperature": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Antidote": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_melee_bleed": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "number"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    },
                    "AppliesTo": {
                      "type": "array"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "AppliesTo",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_melee_blunt": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    },
                    "AppliesTo": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "AppliesTo",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_hultafors": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    },
                    "AppliesTo": {
                      "type": "array"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "AppliesTo",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_vodka_BAD": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "number"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_alyonka": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_slippers": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_knife": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_beer": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Obdolbos2": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_SJ12_TGLabs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_PNB": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Trimadol": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Perfotoran": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              }
            },
            "required": [
              "BuffsAdrenaline",
              "BuffsGoldenStarBalm",
              "BuffsPropital",
              "BuffsSJ1TGLabs",
              "BuffsSJ6TGLabs",
              "BuffsZagustin",
              "Buffs_3bTG",
              "Buffs_AHF1M",
              "Buffs_Antidote",
              "Buffs_BodyTemperature",
              "Buffs_KultistsToxin",
              "Buffs_L1",
              "Buffs_MULE",
              "Buffs_Meldonin",
              "Buffs_Obdolbos",
              "Buffs_Obdolbos2",
              "Buffs_P22",
              "Buffs_PNB",
              "Buffs_Perfotoran",
              "Buffs_SJ12_TGLabs",
              "Buffs_Trimadol",
              "Buffs_drink_aquamari",
              "Buffs_drink_hotrod",
              "Buffs_drink_jack",
              "Buffs_drink_juice_army",
              "Buffs_drink_maxenergy",
              "Buffs_drink_milk",
              "Buffs_drink_moonshine",
              "Buffs_drink_purewater",
              "Buffs_drink_tarcola",
              "Buffs_drink_vodka",
              "Buffs_drink_vodka_BAD",
              "Buffs_drink_water",
              "Buffs_food_alyonka",
              "Buffs_food_beer",
              "Buffs_food_borodinskiye",
              "Buffs_food_condensed_milk",
              "Buffs_food_emelya",
              "Buffs_food_mayonez",
              "Buffs_food_mre",
              "Buffs_food_slippers",
              "Buffs_food_sugar",
              "Buffs_hultafors",
              "Buffs_knife",
              "Buffs_melee_bleed",
              "Buffs_melee_blunt",
              "BuffseTGchange"
            ]
          }
        },
        "required": [
          "Buffs"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/buffs`

## Get a specific buffs

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/buffs?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/buffs?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/buffs?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Buffs": {
            "type": "object",
            "properties": {
              "BuffsSJ1TGLabs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsSJ6TGLabs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsPropital": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsZagustin": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffseTGchange": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsAdrenaline": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "BuffsGoldenStarBalm": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_aquamari": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_maxenergy": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_milk": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_tarcola": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_hotrod": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_juice_army": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_water": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_borodinskiye": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_condensed_milk": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_emelya": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_mayonez": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_mre": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_sugar": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_vodka": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_jack": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_moonshine": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_purewater": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_3bTG": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_AHF1M": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_L1": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_MULE": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Meldonin": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Obdolbos": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "number"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_P22": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_KultistsToxin": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_BodyTemperature": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Antidote": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_melee_bleed": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "number"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    },
                    "AppliesTo": {
                      "type": "array"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "AppliesTo",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_melee_blunt": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    },
                    "AppliesTo": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "AppliesTo",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_hultafors": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    },
                    "AppliesTo": {
                      "type": "array"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "AppliesTo",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_drink_vodka_BAD": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "number"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_alyonka": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_slippers": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_knife": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_food_beer": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "integer"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Obdolbos2": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_SJ12_TGLabs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_PNB": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Trimadol": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              },
              "Buffs_Perfotoran": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "BuffType": {
                      "type": "string"
                    },
                    "Chance": {
                      "type": "integer"
                    },
                    "Delay": {
                      "type": "integer"
                    },
                    "Duration": {
                      "type": "integer"
                    },
                    "Value": {
                      "type": "number"
                    },
                    "AbsoluteValue": {
                      "type": "boolean"
                    },
                    "SkillName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "AbsoluteValue",
                    "BuffType",
                    "Chance",
                    "Delay",
                    "Duration",
                    "SkillName",
                    "Value"
                  ]
                }
              }
            },
            "required": [
              "BuffsAdrenaline",
              "BuffsGoldenStarBalm",
              "BuffsPropital",
              "BuffsSJ1TGLabs",
              "BuffsSJ6TGLabs",
              "BuffsZagustin",
              "Buffs_3bTG",
              "Buffs_AHF1M",
              "Buffs_Antidote",
              "Buffs_BodyTemperature",
              "Buffs_KultistsToxin",
              "Buffs_L1",
              "Buffs_MULE",
              "Buffs_Meldonin",
              "Buffs_Obdolbos",
              "Buffs_Obdolbos2",
              "Buffs_P22",
              "Buffs_PNB",
              "Buffs_Perfotoran",
              "Buffs_SJ12_TGLabs",
              "Buffs_Trimadol",
              "Buffs_drink_aquamari",
              "Buffs_drink_hotrod",
              "Buffs_drink_jack",
              "Buffs_drink_juice_army",
              "Buffs_drink_maxenergy",
              "Buffs_drink_milk",
              "Buffs_drink_moonshine",
              "Buffs_drink_purewater",
              "Buffs_drink_tarcola",
              "Buffs_drink_vodka",
              "Buffs_drink_vodka_BAD",
              "Buffs_drink_water",
              "Buffs_food_alyonka",
              "Buffs_food_beer",
              "Buffs_food_borodinskiye",
              "Buffs_food_condensed_milk",
              "Buffs_food_emelya",
              "Buffs_food_mayonez",
              "Buffs_food_mre",
              "Buffs_food_slippers",
              "Buffs_food_sugar",
              "Buffs_hultafors",
              "Buffs_knife",
              "Buffs_melee_bleed",
              "Buffs_melee_blunt",
              "BuffseTGchange"
            ]
          }
        },
        "required": [
          "Buffs"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/buffs?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# clothing

## Get (all) clothing

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/clothing"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/clothing" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/clothing", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability": {
            "type": "string"
          },
          "Max Durability": {
            "type": "string"
          },
          "Armor Class": {
            "type": "string"
          },
          "Speed Penalty (%)": {
            "type": "string"
          },
          "Mouse Penalty": {
            "type": "string"
          },
          "Ergonomics Penalty": {
            "type": "string"
          },
          "Armor Protection Zones": {
            "type": "string"
          },
          "Indestructibility": {
            "type": "string"
          },
          "FaceShieldMask": {
            "type": "string"
          },
          "Has Hinge": {
            "type": "string"
          },
          "Material Type": {
            "type": "string"
          },
          "Ricochet Params": {
            "type": "string"
          },
          "Deaf Strength": {
            "type": "string"
          },
          "Blunt Throughput": {
            "type": "string"
          },
          "Armor Material": {
            "type": "string"
          },
          "Blindness Protection": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Armor Class",
          "Armor Material",
          "Armor Protection Zones",
          "Blindness Protection",
          "Blunt Throughput",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Deaf Strength",
          "Description",
          "Discard Limit",
          "Durability",
          "Ergonomics Penalty",
          "FaceShieldMask",
          "Has Hinge",
          "Indestructibility",
          "Item ID",
          "Item Weight",
          "Material Type",
          "Max Durability",
          "Max Stack Size",
          "Mouse Penalty",
          "Name",
          "Ricochet Params",
          "Speed Penalty (%)"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/clothing`

## Get a specific clothing

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/clothing?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/clothing?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/clothing?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability": {
            "type": "string"
          },
          "Max Durability": {
            "type": "string"
          },
          "Armor Class": {
            "type": "string"
          },
          "Speed Penalty (%)": {
            "type": "string"
          },
          "Mouse Penalty": {
            "type": "string"
          },
          "Ergonomics Penalty": {
            "type": "string"
          },
          "Armor Protection Zones": {
            "type": "string"
          },
          "Indestructibility": {
            "type": "string"
          },
          "FaceShieldMask": {
            "type": "string"
          },
          "Has Hinge": {
            "type": "string"
          },
          "Material Type": {
            "type": "string"
          },
          "Ricochet Params": {
            "type": "string"
          },
          "Deaf Strength": {
            "type": "string"
          },
          "Blunt Throughput": {
            "type": "string"
          },
          "Armor Material": {
            "type": "string"
          },
          "Blindness Protection": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Armor Class",
          "Armor Material",
          "Armor Protection Zones",
          "Blindness Protection",
          "Blunt Throughput",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Deaf Strength",
          "Description",
          "Discard Limit",
          "Durability",
          "Ergonomics Penalty",
          "FaceShieldMask",
          "Has Hinge",
          "Indestructibility",
          "Item ID",
          "Item Weight",
          "Material Type",
          "Max Durability",
          "Max Stack Size",
          "Mouse Penalty",
          "Name",
          "Ricochet Params",
          "Speed Penalty (%)"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/clothing?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# containers

## Get (all) containers

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/containers"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/containers" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/containers", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Undiscardable": {
            "type": "string"
          },
          "Unsaleable": {
            "type": "string"
          },
          "Can Put Items Into During Raid": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Can Put Items Into During Raid",
          "Cell Height",
          "Cell Width",
          "Description",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Undiscardable",
          "Unsaleable"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/containers`

## Get a specific containers

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/containers?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/containers?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/containers?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Undiscardable": {
            "type": "string"
          },
          "Unsaleable": {
            "type": "string"
          },
          "Can Put Items Into During Raid": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Can Put Items Into During Raid",
          "Cell Height",
          "Cell Width",
          "Description",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Undiscardable",
          "Unsaleable"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/containers?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# firearms

## Get (all) firearms

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/firearms"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/firearms" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/firearms", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Aim Plane": {
            "type": [
              "null",
              "string"
            ]
          },
          "Aim Sensitivity": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Feed": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Jam": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Misfire": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Overheat": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Slide": {
            "type": [
              "null",
              "string"
            ]
          },
          "Malfunction Chance": {
            "type": [
              "null",
              "string"
            ]
          },
          "Base MoA": {
            "type": [
              "null",
              "string"
            ]
          },
          "Burst Shot Count": {
            "type": [
              "null",
              "string"
            ]
          },
          "Camera Recoil": {
            "type": [
              "null",
              "string"
            ]
          },
          "Camera Snap": {
            "type": [
              "null",
              "string"
            ]
          },
          "Can Queue Second Shot": {
            "type": [
              "null",
              "string"
            ]
          },
          "Convergence": {
            "type": [
              "null",
              "string"
            ]
          },
          "Default Ammo": {
            "type": [
              "null",
              "string"
            ]
          },
          "Deviation Curve": {
            "type": [
              "null",
              "string"
            ]
          },
          "Deviation Max": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability Burn Ratio": {
            "type": [
              "null",
              "string"
            ]
          },
          "Ergonomics": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hip Accuracy Restoration Delay": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hip Accuracy Restoration Speed": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hip Innaccuracy Gain": {
            "type": [
              "null",
              "string"
            ]
          },
          "Iron Sight Range": {
            "type": [
              "null",
              "string"
            ]
          },
          "Max Repair Degradation": {
            "type": [
              "null",
              "string"
            ]
          },
          "Min Repair Degradation": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recoil Angle": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recoil Force Back": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recoil Force Up": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recol Dispersion": {
            "type": [
              "null",
              "string"
            ]
          },
          "Sighting Range": {
            "type": [
              "null",
              "string"
            ]
          },
          "Single Fire Rate": {
            "type": [
              "null",
              "string"
            ]
          },
          "Velocity": {
            "type": [
              "null",
              "string"
            ]
          },
          "Effective Distance": {
            "type": [
              "null",
              "string"
            ]
          },
          "Fire Rate": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hearing Distacne": {
            "type": [
              "null",
              "string"
            ]
          },
          "Max Durability on Spawn": {
            "type": [
              "null",
              "string"
            ]
          },
          "Min Durability on Spawn": {
            "type": [
              "null",
              "string"
            ]
          },
          "Weapon Fire Type": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Aim Plane",
          "Aim Sensitivity",
          "Allow Feed",
          "Allow Jam",
          "Allow Misfire",
          "Allow Overheat",
          "Allow Slide",
          "Base MoA",
          "Burst Shot Count",
          "Camera Recoil",
          "Camera Snap",
          "Can Queue Second Shot",
          "Cell Height",
          "Cell Width",
          "Convergence",
          "Default Ammo",
          "Description",
          "Deviation Curve",
          "Deviation Max",
          "Discard Limit",
          "Durability",
          "Durability Burn Ratio",
          "Effective Distance",
          "Ergonomics",
          "Fire Rate",
          "Hearing Distacne",
          "Hip Accuracy Restoration Delay",
          "Hip Accuracy Restoration Speed",
          "Hip Innaccuracy Gain",
          "Iron Sight Range",
          "Item ID",
          "Item Weight",
          "Malfunction Chance",
          "Max Durability on Spawn",
          "Max Repair Degradation",
          "Max Stack Size",
          "Min Durability on Spawn",
          "Min Repair Degradation",
          "Name",
          "Recoil Angle",
          "Recoil Force Back",
          "Recoil Force Up",
          "Recol Dispersion",
          "Sighting Range",
          "Single Fire Rate",
          "Velocity",
          "Weapon Fire Type"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/firearms`

## Get a specific firearms

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/firearms?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/firearms?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/firearms?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Aim Plane": {
            "type": [
              "null",
              "string"
            ]
          },
          "Aim Sensitivity": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Feed": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Jam": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Misfire": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Overheat": {
            "type": [
              "null",
              "string"
            ]
          },
          "Allow Slide": {
            "type": [
              "null",
              "string"
            ]
          },
          "Malfunction Chance": {
            "type": [
              "null",
              "string"
            ]
          },
          "Base MoA": {
            "type": [
              "null",
              "string"
            ]
          },
          "Burst Shot Count": {
            "type": [
              "null",
              "string"
            ]
          },
          "Camera Recoil": {
            "type": [
              "null",
              "string"
            ]
          },
          "Camera Snap": {
            "type": [
              "null",
              "string"
            ]
          },
          "Can Queue Second Shot": {
            "type": [
              "null",
              "string"
            ]
          },
          "Convergence": {
            "type": [
              "null",
              "string"
            ]
          },
          "Default Ammo": {
            "type": [
              "null",
              "string"
            ]
          },
          "Deviation Curve": {
            "type": [
              "null",
              "string"
            ]
          },
          "Deviation Max": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability Burn Ratio": {
            "type": [
              "null",
              "string"
            ]
          },
          "Ergonomics": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hip Accuracy Restoration Delay": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hip Accuracy Restoration Speed": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hip Innaccuracy Gain": {
            "type": [
              "null",
              "string"
            ]
          },
          "Iron Sight Range": {
            "type": [
              "null",
              "string"
            ]
          },
          "Max Repair Degradation": {
            "type": [
              "null",
              "string"
            ]
          },
          "Min Repair Degradation": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recoil Angle": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recoil Force Back": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recoil Force Up": {
            "type": [
              "null",
              "string"
            ]
          },
          "Recol Dispersion": {
            "type": [
              "null",
              "string"
            ]
          },
          "Sighting Range": {
            "type": [
              "null",
              "string"
            ]
          },
          "Single Fire Rate": {
            "type": [
              "null",
              "string"
            ]
          },
          "Velocity": {
            "type": [
              "null",
              "string"
            ]
          },
          "Effective Distance": {
            "type": [
              "null",
              "string"
            ]
          },
          "Fire Rate": {
            "type": [
              "null",
              "string"
            ]
          },
          "Hearing Distacne": {
            "type": [
              "null",
              "string"
            ]
          },
          "Max Durability on Spawn": {
            "type": [
              "null",
              "string"
            ]
          },
          "Min Durability on Spawn": {
            "type": [
              "null",
              "string"
            ]
          },
          "Weapon Fire Type": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Aim Plane",
          "Aim Sensitivity",
          "Allow Feed",
          "Allow Jam",
          "Allow Misfire",
          "Allow Overheat",
          "Allow Slide",
          "Base MoA",
          "Burst Shot Count",
          "Camera Recoil",
          "Camera Snap",
          "Can Queue Second Shot",
          "Cell Height",
          "Cell Width",
          "Convergence",
          "Default Ammo",
          "Description",
          "Deviation Curve",
          "Deviation Max",
          "Discard Limit",
          "Durability",
          "Durability Burn Ratio",
          "Effective Distance",
          "Ergonomics",
          "Fire Rate",
          "Hearing Distacne",
          "Hip Accuracy Restoration Delay",
          "Hip Accuracy Restoration Speed",
          "Hip Innaccuracy Gain",
          "Iron Sight Range",
          "Item ID",
          "Item Weight",
          "Malfunction Chance",
          "Max Durability on Spawn",
          "Max Repair Degradation",
          "Max Stack Size",
          "Min Durability on Spawn",
          "Min Repair Degradation",
          "Name",
          "Recoil Angle",
          "Recoil Force Back",
          "Recoil Force Up",
          "Recol Dispersion",
          "Sighting Range",
          "Single Fire Rate",
          "Velocity",
          "Weapon Fire Type"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/firearms?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# food

## Get (all) food

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/food"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/food" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/food", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Use Time": {
            "type": "string"
          },
          "Effect Type": {
            "type": "string"
          },
          "Max Resource": {
            "type": "string"
          },
          "Stimulator Buffs": {
            "type": "string"
          },
          "Health Effects": {
            "type": "string"
          },
          "Removes Effects": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Effect Type",
          "Health Effects",
          "Item ID",
          "Item Weight",
          "Max Resource",
          "Max Stack Size",
          "Name",
          "Removes Effects",
          "Stimulator Buffs",
          "Use Time"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/food`

## Get a specific food

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/food?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/food?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/food?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Use Time": {
            "type": "string"
          },
          "Effect Type": {
            "type": "string"
          },
          "Max Resource": {
            "type": "string"
          },
          "Stimulator Buffs": {
            "type": "string"
          },
          "Health Effects": {
            "type": "string"
          },
          "Removes Effects": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Effect Type",
          "Health Effects",
          "Item ID",
          "Item Weight",
          "Max Resource",
          "Max Stack Size",
          "Name",
          "Removes Effects",
          "Stimulator Buffs",
          "Use Time"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/food?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# grenades

## Get (all) grenades

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/grenades"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/grenades" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/grenades", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Can Be Hidden During Throw": {
            "type": "string"
          },
          "Contusion Distance": {
            "type": "string"
          },
          "Explosion Delay": {
            "type": "string"
          },
          "Fragments Count": {
            "type": "string"
          },
          "Max Explosion Distance": {
            "type": "string"
          },
          "Min Explosion Distance": {
            "type": "string"
          },
          "Strength": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Can Be Hidden During Throw",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Contusion Distance",
          "Description",
          "Discard Limit",
          "Explosion Delay",
          "Fragments Count",
          "Item ID",
          "Item Weight",
          "Max Explosion Distance",
          "Max Stack Size",
          "Min Explosion Distance",
          "Name",
          "Strength"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/grenades`

## Get a specific grenades

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/grenades?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/grenades?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/grenades?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Can Be Hidden During Throw": {
            "type": "string"
          },
          "Contusion Distance": {
            "type": "string"
          },
          "Explosion Delay": {
            "type": "string"
          },
          "Fragments Count": {
            "type": "string"
          },
          "Max Explosion Distance": {
            "type": "string"
          },
          "Min Explosion Distance": {
            "type": "string"
          },
          "Strength": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Can Be Hidden During Throw",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Contusion Distance",
          "Description",
          "Discard Limit",
          "Explosion Delay",
          "Fragments Count",
          "Item ID",
          "Item Weight",
          "Max Explosion Distance",
          "Max Stack Size",
          "Min Explosion Distance",
          "Name",
          "Strength"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/grenades?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# headphones

## Get (all) headphones

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/headphones"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/headphones" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/headphones", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Blocks Earpiece": {
            "type": "string"
          },
          "Blocks Eyewear": {
            "type": "string"
          },
          "Blocks Headwear": {
            "type": "string"
          },
          "Blocks Face Cover": {
            "type": "string"
          },
          "Distortion": {
            "type": "string"
          },
          "Compressor Treshold": {
            "type": "string"
          },
          "Compressor Attack": {
            "type": "string"
          },
          "Compressor Release": {
            "type": "string"
          },
          "Compressor Gain": {
            "type": "string"
          },
          "Cutoff Frequency": {
            "type": "string"
          },
          "Resonance": {
            "type": "string"
          },
          "Compressor Volume": {
            "type": "string"
          },
          "Ambient Volume": {
            "type": "string"
          },
          "Dry Volume": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Ambient Volume",
          "Blocks Earpiece",
          "Blocks Eyewear",
          "Blocks Face Cover",
          "Blocks Headwear",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Compressor Attack",
          "Compressor Gain",
          "Compressor Release",
          "Compressor Treshold",
          "Compressor Volume",
          "Cutoff Frequency",
          "Description",
          "Discard Limit",
          "Distortion",
          "Dry Volume",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Resonance"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/headphones`

## Get a specific headphones

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/headphones?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/headphones?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/headphones?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Blocks Earpiece": {
            "type": "string"
          },
          "Blocks Eyewear": {
            "type": "string"
          },
          "Blocks Headwear": {
            "type": "string"
          },
          "Blocks Face Cover": {
            "type": "string"
          },
          "Distortion": {
            "type": "string"
          },
          "Compressor Treshold": {
            "type": "string"
          },
          "Compressor Attack": {
            "type": "string"
          },
          "Compressor Release": {
            "type": "string"
          },
          "Compressor Gain": {
            "type": "string"
          },
          "Cutoff Frequency": {
            "type": "string"
          },
          "Resonance": {
            "type": "string"
          },
          "Compressor Volume": {
            "type": "string"
          },
          "Ambient Volume": {
            "type": "string"
          },
          "Dry Volume": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Ambient Volume",
          "Blocks Earpiece",
          "Blocks Eyewear",
          "Blocks Face Cover",
          "Blocks Headwear",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Compressor Attack",
          "Compressor Gain",
          "Compressor Release",
          "Compressor Treshold",
          "Compressor Volume",
          "Cutoff Frequency",
          "Description",
          "Discard Limit",
          "Distortion",
          "Dry Volume",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "Resonance"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/headphones?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# helmets

## Get (all) helmets

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/helmets"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/helmets" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/helmets", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Armor Class": {
            "type": "string"
          },
          "Materials": {
            "type": "string"
          },
          "Blindness Protection": {
            "type": "string"
          },
          "Blocks Earpiece": {
            "type": "string"
          },
          "Blocks Eyewear": {
            "type": "string"
          },
          "Blocks FaceCover": {
            "type": "string"
          },
          "Blocks Headwear": {
            "type": "string"
          },
          "Blunt Throughput": {
            "type": "string"
          },
          "Max Durability": {
            "type": "string"
          },
          "Repair Cost": {
            "type": "string"
          },
          "Protection Zones": {
            "type": "string"
          },
          "Armor Segments": {
            "type": "string"
          },
          "Movement Speed Penalty": {
            "type": "string"
          },
          "Turn Speed Penalty": {
            "type": "string"
          },
          "Ergonomics Penalty": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Armor Class",
          "Armor Segments",
          "Blindness Protection",
          "Blocks Earpiece",
          "Blocks Eyewear",
          "Blocks FaceCover",
          "Blocks Headwear",
          "Blunt Throughput",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Ergonomics Penalty",
          "Item ID",
          "Item Weight",
          "Materials",
          "Max Durability",
          "Max Stack Size",
          "Movement Speed Penalty",
          "Name",
          "Protection Zones",
          "Repair Cost",
          "Turn Speed Penalty"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/helmets`

## Get a specific helmets

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/helmets?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/helmets?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/helmets?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Armor Class": {
            "type": "string"
          },
          "Materials": {
            "type": "string"
          },
          "Blindness Protection": {
            "type": "string"
          },
          "Blocks Earpiece": {
            "type": "string"
          },
          "Blocks Eyewear": {
            "type": "string"
          },
          "Blocks FaceCover": {
            "type": "string"
          },
          "Blocks Headwear": {
            "type": "string"
          },
          "Blunt Throughput": {
            "type": "string"
          },
          "Max Durability": {
            "type": "string"
          },
          "Repair Cost": {
            "type": "string"
          },
          "Protection Zones": {
            "type": "string"
          },
          "Armor Segments": {
            "type": "string"
          },
          "Movement Speed Penalty": {
            "type": "string"
          },
          "Turn Speed Penalty": {
            "type": "string"
          },
          "Ergonomics Penalty": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Armor Class",
          "Armor Segments",
          "Blindness Protection",
          "Blocks Earpiece",
          "Blocks Eyewear",
          "Blocks FaceCover",
          "Blocks Headwear",
          "Blunt Throughput",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Ergonomics Penalty",
          "Item ID",
          "Item Weight",
          "Materials",
          "Max Durability",
          "Max Stack Size",
          "Movement Speed Penalty",
          "Name",
          "Protection Zones",
          "Repair Cost",
          "Turn Speed Penalty"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/helmets?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# items

## Get (all) items

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/items"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/items" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/items", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "ShortName": {
            "type": [
              "null",
              "string"
            ]
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "props": {
            "type": "string"
          }
        },
        "required": [
          "Description",
          "Item ID",
          "Name",
          "ShortName",
          "props"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/items`

## Get a specific items

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/items?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/items?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/items?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "ShortName": {
            "type": [
              "null",
              "string"
            ]
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "props": {
            "type": "string"
          }
        },
        "required": [
          "Description",
          "Item ID",
          "Name",
          "ShortName",
          "props"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/items?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# limits

## Get (all) limits

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/limits"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/limits" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/limits", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "template_name": {
            "type": "string"
          },
          "template_value": {
            "type": "integer"
          }
        },
        "required": [
          "template_name",
          "template_value"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/limits`

## Get a specific limits

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/limits?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/limits?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/limits?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "template_name": {
            "type": "string"
          },
          "template_value": {
            "type": "integer"
          }
        },
        "required": [
          "template_name",
          "template_value"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/limits?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# karma

## Get (all) karma

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/karma"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/karma" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/karma", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Karma Info": {
            "type": "object",
            "properties": {
              "-7": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-6": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-5": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-4": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-3": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-2": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-1": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "0": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "integer"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "1": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "2": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "3": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "4": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "5": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "6": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              }
            },
            "required": [
              "-1",
              "-2",
              "-3",
              "-4",
              "-5",
              "-6",
              "-7",
              "0",
              "1",
              "2",
              "3",
              "4",
              "5",
              "6"
            ]
          }
        },
        "required": [
          "Karma Info"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/karma`

## Get a specific karma

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/karma?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/karma?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/karma?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Karma Info": {
            "type": "object",
            "properties": {
              "-7": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-6": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-5": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-4": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-3": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-2": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "-1": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "0": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "integer"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "integer"
                  },
                  "PaidExitCostModifier": {
                    "type": "integer"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "integer"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "integer"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "1": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "2": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "3": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "4": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "5": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              },
              "6": {
                "type": "object",
                "properties": {
                  "SavageCooldownModifier": {
                    "type": "number"
                  },
                  "ScavCaseTimeModifier": {
                    "type": "number"
                  },
                  "PaidExitCostModifier": {
                    "type": "number"
                  },
                  "BotFollowChance": {
                    "type": "integer"
                  },
                  "ScavEquipmentSpawnChanceModifier": {
                    "type": "integer"
                  },
                  "PriceModifier": {
                    "type": "number"
                  },
                  "HostileBosses": {
                    "type": "boolean"
                  },
                  "HostileScavs": {
                    "type": "boolean"
                  },
                  "ScavAttackSupport": {
                    "type": "boolean"
                  },
                  "ExfiltrationPriceModifier": {
                    "type": "number"
                  },
                  "AvailableExits": {
                    "type": "integer"
                  }
                },
                "required": [
                  "AvailableExits",
                  "BotFollowChance",
                  "ExfiltrationPriceModifier",
                  "HostileBosses",
                  "HostileScavs",
                  "PaidExitCostModifier",
                  "PriceModifier",
                  "SavageCooldownModifier",
                  "ScavAttackSupport",
                  "ScavCaseTimeModifier",
                  "ScavEquipmentSpawnChanceModifier"
                ]
              }
            },
            "required": [
              "-1",
              "-2",
              "-3",
              "-4",
              "-5",
              "-6",
              "-7",
              "0",
              "1",
              "2",
              "3",
              "4",
              "5",
              "6"
            ]
          }
        },
        "required": [
          "Karma Info"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/karma?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# knives

## Get (all) knives

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/knives"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/knives" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/knives", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Deflection Consumption": {
            "type": "string"
          },
          "Durability": {
            "type": "string"
          },
          "Max Repair Degradation": {
            "type": "string"
          },
          "Min Repair Degradation": {
            "type": "string"
          },
          "Primary Consumption": {
            "type": "string"
          },
          "Primary Distance": {
            "type": "string"
          },
          "Secondry Consumption": {
            "type": "string"
          },
          "Secondry Distance": {
            "type": "string"
          },
          "Slash Penetration": {
            "type": "string"
          },
          "Stab Penetration": {
            "type": "string"
          },
          "Unlootable": {
            "type": "string"
          },
          "Hit Delay": {
            "type": "string"
          },
          "Hit Radius": {
            "type": "string"
          },
          "Hit Slash Damage": {
            "type": "string"
          },
          "Hit Slash Rate": {
            "type": "string"
          },
          "Hit Stab Damage": {
            "type": "string"
          },
          "Hit Stab Rate": {
            "type": "string"
          },
          "Poison Charges": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Deflection Consumption",
          "Description",
          "Discard Limit",
          "Durability",
          "Hit Delay",
          "Hit Radius",
          "Hit Slash Damage",
          "Hit Slash Rate",
          "Hit Stab Damage",
          "Hit Stab Rate",
          "Item ID",
          "Item Weight",
          "Max Repair Degradation",
          "Max Stack Size",
          "Min Repair Degradation",
          "Name",
          "Poison Charges",
          "Primary Consumption",
          "Primary Distance",
          "Secondry Consumption",
          "Secondry Distance",
          "Slash Penetration",
          "Stab Penetration",
          "Unlootable"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/knives`

## Get a specific knives

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/knives?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/knives?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/knives?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Deflection Consumption": {
            "type": "string"
          },
          "Durability": {
            "type": "string"
          },
          "Max Repair Degradation": {
            "type": "string"
          },
          "Min Repair Degradation": {
            "type": "string"
          },
          "Primary Consumption": {
            "type": "string"
          },
          "Primary Distance": {
            "type": "string"
          },
          "Secondry Consumption": {
            "type": "string"
          },
          "Secondry Distance": {
            "type": "string"
          },
          "Slash Penetration": {
            "type": "string"
          },
          "Stab Penetration": {
            "type": "string"
          },
          "Unlootable": {
            "type": "string"
          },
          "Hit Delay": {
            "type": "string"
          },
          "Hit Radius": {
            "type": "string"
          },
          "Hit Slash Damage": {
            "type": "string"
          },
          "Hit Slash Rate": {
            "type": "string"
          },
          "Hit Stab Damage": {
            "type": "string"
          },
          "Hit Stab Rate": {
            "type": "string"
          },
          "Poison Charges": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Deflection Consumption",
          "Description",
          "Discard Limit",
          "Durability",
          "Hit Delay",
          "Hit Radius",
          "Hit Slash Damage",
          "Hit Slash Rate",
          "Hit Stab Damage",
          "Hit Stab Rate",
          "Item ID",
          "Item Weight",
          "Max Repair Degradation",
          "Max Stack Size",
          "Min Repair Degradation",
          "Name",
          "Poison Charges",
          "Primary Consumption",
          "Primary Distance",
          "Secondry Consumption",
          "Secondry Distance",
          "Slash Penetration",
          "Stab Penetration",
          "Unlootable"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/knives?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# keys

## Get (all) keys

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/keys"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/keys" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/keys", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Fixed Price": {
            "type": "null"
          },
          "Unlootable": {
            "type": "string"
          },
          "Discarding Block": {
            "type": "string"
          },
          "MaximumNumber Of Usage": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Discarding Block",
          "Fixed Price",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "MaximumNumber Of Usage",
          "Name",
          "Unlootable"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/keys`

## Get a specific keys

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/keys?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/keys?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/keys?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Fixed Price": {
            "type": "null"
          },
          "Unlootable": {
            "type": "string"
          },
          "Discarding Block": {
            "type": "string"
          },
          "MaximumNumber Of Usage": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Discarding Block",
          "Fixed Price",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "MaximumNumber Of Usage",
          "Name",
          "Unlootable"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/keys?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# limits

## Get (all) limits

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/limits"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/limits" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/limits", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "template_name": {
            "type": "string"
          },
          "template_value": {
            "type": "integer"
          }
        },
        "required": [
          "template_name",
          "template_value"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/limits`

## Get a specific limits

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/limits?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/limits?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/limits?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "template_name": {
            "type": "string"
          },
          "template_value": {
            "type": "integer"
          }
        },
        "required": [
          "template_name",
          "template_value"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/limits?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# maps

## Get (all) maps

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/maps"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/maps" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/maps", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Map Enabled": {
            "type": "boolean"
          },
          "Map Locked": {
            "type": "boolean"
          },
          "Map Internal Name": {
            "type": "string"
          },
          "Avg. Player Level": {
            "type": "number"
          },
          "Raid Timer": {
            "type": "integer"
          },
          "Max Players": {
            "type": "number"
          },
          "Min Players": {
            "type": "number"
          },
          "Required Player Level": {
            "type": "number"
          }
        },
        "required": [
          "Avg. Player Level",
          "Map Enabled",
          "Map Internal Name",
          "Map Locked",
          "Max Players",
          "Min Players",
          "Name",
          "Raid Timer",
          "Required Player Level"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/maps`

## Get a specific maps

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/maps?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/maps?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/maps?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Map Enabled": {
            "type": "boolean"
          },
          "Map Locked": {
            "type": "boolean"
          },
          "Map Internal Name": {
            "type": "string"
          },
          "Avg. Player Level": {
            "type": "number"
          },
          "Raid Timer": {
            "type": "integer"
          },
          "Max Players": {
            "type": "number"
          },
          "Min Players": {
            "type": "number"
          },
          "Required Player Level": {
            "type": "number"
          }
        },
        "required": [
          "Avg. Player Level",
          "Map Enabled",
          "Map Internal Name",
          "Map Locked",
          "Max Players",
          "Min Players",
          "Name",
          "Raid Timer",
          "Required Player Level"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/maps?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# magazines

## Get (all) magazines

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/magazines"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/magazines" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/magazines", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Accuracy": {
            "type": "string"
          },
          "Check Time Modifier": {
            "type": "string"
          },
          "Durability": {
            "type": "string"
          },
          "Ergonomics": {
            "type": "string"
          },
          "Load  Unload Modifier": {
            "type": "string"
          },
          "Loudness": {
            "type": "string"
          },
          "Moddable in Raid": {
            "type": "string"
          },
          "Recoil": {
            "type": "string"
          },
          "Reload Mag Type": {
            "type": "string"
          },
          "Velocity": {
            "type": "string"
          },
          "Visible Ammo Ranges": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Accuracy",
          "Cell Height",
          "Cell Width",
          "Check Time Modifier",
          "Description",
          "Discard Limit",
          "Durability",
          "Ergonomics",
          "Item ID",
          "Item Weight",
          "Load  Unload Modifier",
          "Loudness",
          "Max Stack Size",
          "Moddable in Raid",
          "Name",
          "Recoil",
          "Reload Mag Type",
          "Velocity",
          "Visible Ammo Ranges"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/magazines`

## Get a specific magazines

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/magazines?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/magazines?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/magazines?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Accuracy": {
            "type": "string"
          },
          "Check Time Modifier": {
            "type": "string"
          },
          "Durability": {
            "type": "string"
          },
          "Ergonomics": {
            "type": "string"
          },
          "Load  Unload Modifier": {
            "type": "string"
          },
          "Loudness": {
            "type": "string"
          },
          "Moddable in Raid": {
            "type": "string"
          },
          "Recoil": {
            "type": "string"
          },
          "Reload Mag Type": {
            "type": "string"
          },
          "Velocity": {
            "type": "string"
          },
          "Visible Ammo Ranges": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          "Accuracy",
          "Cell Height",
          "Cell Width",
          "Check Time Modifier",
          "Description",
          "Discard Limit",
          "Durability",
          "Ergonomics",
          "Item ID",
          "Item Weight",
          "Load  Unload Modifier",
          "Loudness",
          "Max Stack Size",
          "Moddable in Raid",
          "Name",
          "Recoil",
          "Reload Mag Type",
          "Velocity",
          "Visible Ammo Ranges"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/magazines?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# medicals

## Get (all) medicals

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/medicals"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/medicals" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/medicals", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Use Time": {
            "type": [
              "null",
              "string"
            ]
          },
          "Effect Type": {
            "type": [
              "null",
              "string"
            ]
          },
          "Max Uses": {
            "type": [
              "null",
              "string"
            ]
          },
          "Resource Consumption Rate": {
            "type": [
              "null",
              "string"
            ]
          },
          "Stimulator Buffs": {
            "type": [
              "null",
              "string"
            ]
          },
          " Health Effects": {
            "type": [
              "null",
              "string"
            ]
          },
          "Removes Effects": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          " Health Effects",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Effect Type",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Max Uses",
          "Name",
          "Removes Effects",
          "Resource Consumption Rate",
          "Stimulator Buffs",
          "Use Time"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/medicals`

## Get a specific medicals

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/medicals?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/medicals?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/medicals?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Use Time": {
            "type": [
              "null",
              "string"
            ]
          },
          "Effect Type": {
            "type": [
              "null",
              "string"
            ]
          },
          "Max Uses": {
            "type": [
              "null",
              "string"
            ]
          },
          "Resource Consumption Rate": {
            "type": [
              "null",
              "string"
            ]
          },
          "Stimulator Buffs": {
            "type": [
              "null",
              "string"
            ]
          },
          " Health Effects": {
            "type": [
              "null",
              "string"
            ]
          },
          "Removes Effects": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          }
        },
        "required": [
          " Health Effects",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Effect Type",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Max Uses",
          "Name",
          "Removes Effects",
          "Resource Consumption Rate",
          "Stimulator Buffs",
          "Use Time"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/medicals?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# mods

## Get (all) mods

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/mods"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/mods" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/mods", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability": {
            "type": "string"
          },
          "Accuracy": {
            "type": "string"
          },
          "Recoil": {
            "type": "string"
          },
          "Loudness": {
            "type": "string"
          },
          "Effective Distance": {
            "type": "string"
          },
          "Ergonomics": {
            "type": "string"
          },
          "Velocity": {
            "type": "string"
          },
          "Modable in Raid": {
            "type": "string"
          },
          "Sighting Range": {
            "type": "string"
          },
          "Heat Factor": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Accuracy",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Durability",
          "Effective Distance",
          "Ergonomics",
          "Heat Factor",
          "Item ID",
          "Item Weight",
          "Loudness",
          "Max Stack Size",
          "Modable in Raid",
          "Name",
          "Recoil",
          "Sighting Range",
          "Velocity"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/mods`

## Get a specific mods

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/mods?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/mods?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/mods?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": [
              "null",
              "string"
            ]
          },
          "Durability": {
            "type": "string"
          },
          "Accuracy": {
            "type": "string"
          },
          "Recoil": {
            "type": "string"
          },
          "Loudness": {
            "type": "string"
          },
          "Effective Distance": {
            "type": "string"
          },
          "Ergonomics": {
            "type": "string"
          },
          "Velocity": {
            "type": "string"
          },
          "Modable in Raid": {
            "type": "string"
          },
          "Sighting Range": {
            "type": "string"
          },
          "Heat Factor": {
            "type": [
              "null",
              "string"
            ]
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          },
          "Can be sold on flea market": {
            "type": "string"
          },
          "Discard Limit": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          }
        },
        "required": [
          "Accuracy",
          "Can be sold on flea market",
          "Cell Height",
          "Cell Width",
          "Description",
          "Discard Limit",
          "Durability",
          "Effective Distance",
          "Ergonomics",
          "Heat Factor",
          "Item ID",
          "Item Weight",
          "Loudness",
          "Max Stack Size",
          "Modable in Raid",
          "Name",
          "Recoil",
          "Sighting Range",
          "Velocity"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/mods?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# money

## Get (all) money

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/money"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/money" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/money", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "type"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/money`

## Get a specific money

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/money?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/money?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/money?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Name": {
            "type": "string"
          },
          "Item ID": {
            "type": "string"
          },
          "Description": {
            "type": "string"
          },
          "Max Stack Size": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "Cell Height": {
            "type": "string"
          },
          "Cell Width": {
            "type": "string"
          },
          "Item Weight": {
            "type": "string"
          }
        },
        "required": [
          "Cell Height",
          "Cell Width",
          "Description",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Name",
          "type"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/money?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# rig

## Get (all) rig

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/rig"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/rig" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/rig", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    }
  },
  "required": [
    "title"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/rig`

## Get a specific rig

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/rig?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/rig?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/rig?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    }
  },
  "required": [
    "title"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/rig?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

# traderResets

## Get (all) traderResets

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/traderResets"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/traderresets" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/traderResets", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    }
  },
  "required": [
    "title"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/traderresets`

## Get a specific traderResets

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/traderResets?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/traderresets?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/traderResets?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    }
  },
  "required": [
    "title"
  ]
}
```

### HTTP Request

`GET https://https://api.tarkov-changes.com/v1/traderresets?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for


# Search

## Search for a specific item

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/search?query=foo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/search?query=foo" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/search?query=foo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "hit": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "full_url": {
            "type": "string"
          }
        },
        "required": [
          "full_url",
          "hit",
          "type"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://api.tarkov-changes.com/v1/search?query=killa`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for


# Weather

## Get up to date weather information

```python
import requests
import json

url = "https://api.tarkov-changes.com/v1/weather"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': auth_token
}

response = requests.get("GET", url, headers=headers)

print(response.text)
```

```shell
curl "https://api.tarkov-changes.com/v1/weather" -H "AUTH-Token: $sometoken"
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("AUTH-Token", $auth_token);

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.tarkov-changes.com/v1/weather", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> The above command returns the following structure:

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "timestamp": {
            "type": "integer"
          },
          "cloud": {
            "type": "number"
          },
          "wind_speed": {
            "type": "integer"
          },
          "wind_direction": {
            "type": "integer"
          },
          "wind_gustiness": {
            "type": "number"
          },
          "rain": {
            "type": "integer"
          },
          "rain_intensity": {
            "type": "number"
          },
          "fog": {
            "type": "number"
          },
          "temp": {
            "type": "integer"
          },
          "pressure": {
            "type": "integer"
          },
          "date": {
            "type": "string"
          },
          "time": {
            "type": "string"
          }
        },
        "required": [
          "cloud",
          "date",
          "fog",
          "pressure",
          "rain",
          "rain_intensity",
          "temp",
          "time",
          "timestamp",
          "wind_direction",
          "wind_gustiness",
          "wind_speed"
        ]
      }
    }
  },
  "required": [
    "msg",
    "results",
    "status"
  ]
}
```

### HTTP Request

`GET https://api.tarkov-changes.com/v1/weather`


