import requests

URL = 'https://api.github.com'
headers = {'Authorization': 'Bearer 31a31e5f784d9cef38dc9de765365cb744c624be'}

response = requests.get(URL + '/user/following', headers=headers)

print(response)
print(response.text)

lkh-1-1
bks-1-2
bks-1-2

_______________
|  id  | name |
---------------
|      |      |


post '임근혁.com/user' { id: 'lkh', name: '임근학' }