import requests

out = requests.get("http://127.0.0.1:5000")
print(out.text)