import requests

r = requests.get('https://amazon.com')
print(r.text)