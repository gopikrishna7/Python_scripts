import requests


r = requests.get("http://example.com")

if r.status_code==200:
    print("Everything Looks Good!")
else:
    print("Something went wrong!")