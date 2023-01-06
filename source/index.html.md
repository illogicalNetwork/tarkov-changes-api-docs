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
import requests

auth_token = requests.get("https://api.tarkov-changes.com/v1/auth").json().get("CSRF-Token")
```

```shell
curl "https://api.tarkov-changes.com/v1/auth"
```

```javascript
```

# Armor

## Get All Armor

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/armor", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/armor" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Armor

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

`GET https://https://api.tarkov-changes.com/v1/armor?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Backpacks

## Get All Backpacks

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/backpacks", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/backpacks" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Backpacks

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

`GET https://https://api.tarkov-changes.com/v1/backpacks?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Banned

## Get All Banned

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/banned", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/banned" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Banned

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

`GET https://https://api.tarkov-changes.com/v1/banned?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Barters

## Get All Barters

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/barters", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/barters" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Barters

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

`GET https://https://api.tarkov-changes.com/v1/barters?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Boss

## Get All Boss

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/boss", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/boss" -H "CSRF-Token: $sometoken"
```

```javascript
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
          "Map": {
            "type": "string"
          },
          "MAP_ID": {
            "type": "string"
          },
          "BossName": {
            "type": "string"
          },
          "BossChance": {
            "type": "number"
          },
          "BossZone": {
            "type": "string"
          },
          "BossEscortDifficult": {
            "type": "string"
          },
          "BossEscortAmount": {
            "type": "string"
          }
        },
        "required": [
          "BossChance",
          "BossEscortAmount",
          "BossEscortDifficult",
          "BossName",
          "BossZone",
          "MAP_ID",
          "Map"
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

`GET https://https://api.tarkov-changes.com/v1/boss`

## Get a specific Boss

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

`GET https://https://api.tarkov-changes.com/v1/boss?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Buffs

## Get All Buffs

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/buffs", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/buffs" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Buffs

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

`GET https://https://api.tarkov-changes.com/v1/buffs?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Credits

## Get All Credits

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/credits", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/credits" -H "CSRF-Token: $sometoken"
```

```javascript
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
          "bsg_id": {
            "type": "string"
          },
          "baseValue": {
            "type": "integer"
          }
        },
        "required": [
          "baseValue",
          "bsg_id"
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

`GET https://https://api.tarkov-changes.com/v1/credits`

## Get a specific Credits

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

`GET https://https://api.tarkov-changes.com/v1/credits?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Clothing

## Get All Clothing

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/clothing", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/clothing" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Clothing

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

`GET https://https://api.tarkov-changes.com/v1/clothing?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Containers

## Get All Containers

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/containers", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/containers" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Containers

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

`GET https://https://api.tarkov-changes.com/v1/containers?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Firearms

## Get All Firearms

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/firearms", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/firearms" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Firearms

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

`GET https://https://api.tarkov-changes.com/v1/firearms?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Food

## Get All Food

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/food", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/food" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Food

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

`GET https://https://api.tarkov-changes.com/v1/food?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Grenades

## Get All Grenades

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/grenades", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/grenades" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Grenades

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

`GET https://https://api.tarkov-changes.com/v1/grenades?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Headphones

## Get All Headphones

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/headphones", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/headphones" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Headphones

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

`GET https://https://api.tarkov-changes.com/v1/headphones?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Helmets

## Get All Helmets

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/helmets", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/helmets" -H "CSRF-Token: $sometoken"
```

```javascript
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

`GET https://https://api.tarkov-changes.com/v1/helmets`

## Get a specific Helmets

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

`GET https://https://api.tarkov-changes.com/v1/helmets?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Items

## Get All Items

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/items", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/items" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Items

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

`GET https://https://api.tarkov-changes.com/v1/items?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Limits

## Get All Limits

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/limits", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/limits" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Limits

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

`GET https://https://api.tarkov-changes.com/v1/limits?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Karma

## Get All Karma

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/karma", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/karma" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Karma

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

`GET https://https://api.tarkov-changes.com/v1/karma?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Knives

## Get All Knives

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/knives", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/knives" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Knives

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

`GET https://https://api.tarkov-changes.com/v1/knives?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Keys

## Get All Keys

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/keys", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/keys" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Keys

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

`GET https://https://api.tarkov-changes.com/v1/keys?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Maps

## Get All Maps

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/maps", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/maps" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Maps

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

`GET https://https://api.tarkov-changes.com/v1/maps?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Magazines

## Get All Magazines

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/magazines", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/magazines" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Magazines

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

`GET https://https://api.tarkov-changes.com/v1/magazines?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Medicals

## Get All Medicals

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/medicals", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/medicals" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Medicals

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

`GET https://https://api.tarkov-changes.com/v1/medicals?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Mods

## Get All Mods

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/mods", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/mods" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Mods

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

`GET https://https://api.tarkov-changes.com/v1/mods?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Money

## Get All Money

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/money", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/money" -H "CSRF-Token: $sometoken"
```

```javascript
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

## Get a specific Money

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

`GET https://https://api.tarkov-changes.com/v1/money?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Rigs

## Get All Rigs

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/rigs", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/rigs" -H "CSRF-Token: $sometoken"
```

```javascript
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
          "Blocks Armor Vest": {
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
          "Blunt Throughput": {
            "type": "string"
          },
          "Armor Material": {
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
          "Armor Material",
          "Blocks Armor Vest",
          "Blunt Throughput",
          "Cell Height",
          "Cell Width",
          "Description",
          "Ergonomics Penalty",
          "Item ID",
          "Item Weight",
          "Max Stack Size",
          "Mouse Penalty",
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

`GET https://https://api.tarkov-changes.com/v1/rigs`

## Get a specific Rigs

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

`GET https://https://api.tarkov-changes.com/v1/rigs?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Search

## Get All Search

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/search", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/search" -H "CSRF-Token: $sometoken"
```

```javascript
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
      "type": "array"
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

`GET https://https://api.tarkov-changes.com/v1/search`

## Get a specific Search

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

`GET https://https://api.tarkov-changes.com/v1/search?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Trader Resets

## Get All Trader Resets

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/trader resets", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/trader resets" -H "CSRF-Token: $sometoken"
```

```javascript
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

`GET https://https://api.tarkov-changes.com/v1/trader resets`

## Get a specific Trader Resets

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

`GET https://https://api.tarkov-changes.com/v1/trader resets?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###
# Weather

## Get All Weather

```python
import requests

headers = { "CSRF-Token": auth_token }

auth_token = requests.get("https://api.tarkov-changes.com/v1/weather", headers=headers)
```

```shell
curl "https://api.tarkov-changes.com/v1/weather" -H "CSRF-Token: $sometoken"
```

```javascript
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

`GET https://https://api.tarkov-changes.com/v1/weather`

## Get a specific Weather

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

`GET https://https://api.tarkov-changes.com/v1/weather?query=foo`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
query | false | Include the item or search term you wish to search for

###

