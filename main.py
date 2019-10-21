import requests

URL = 'https://api.github.com'
headers = {'Authorization': 'Bearer 31a31e5f784d9cef38dc9de765365cb744c624be'}

response = requests.get(URL + '/user/following', headers=headers)

print(response)
print(response.text)