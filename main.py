import sys

import requests
print(str(sys.argv[1]))
r = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(sys.argv[1]) + '/')
if r.status_code >= 200 and r.status_code < 300:
    x = r.json()
    print("Name: " + x["name"])
    print("Types:")
    for a in x["types"]:
        print("  - Name:" + a["type"]["name"]),
    print("Weight: " + str(x["weight"]))

else:
    print("ilgili adrese erişilmedi")
