import requests

new = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 101,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "bob",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print(new.text)

change = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 101,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "fluppy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 2,
      "name": "string"
    }
  ],
  "status": "available"
})

print(change.text)


catch = requests.get("https://petstore.swagger.io/v2/pet/101")

print(catch.text)