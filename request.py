import requests


url = 'http://127.0.0.1:10000/script'

def create_request(json):
    headers = {'content-type': 'application/json'}
    print(json)
    r = requests.post(url, json=json, headers=headers, timeout=1)
    print(r.json())


if __name__ == '__main__':

    create_request(dict({
    "nameScript": "script.py",
    "params" : {
        "nbMax" : 50,
        "nbMini": 1,
        "lenght": 50
    }
}))