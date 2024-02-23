import requests

r = requests.get("http:")

with open("1hello.txt", "w") as f:
    print(r, file=f)
