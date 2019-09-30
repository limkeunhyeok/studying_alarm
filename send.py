import requests, json

# Get tag data from github
GITHUB_URL = 'https://api.github.com/repos/limkeunhyeok/algorithm-study/tags'
apiResults = requests.get(GITHUB_URL)
texts = apiResults.json()

users = {'lkh':0, 'bks':0, 'lhs':0, 'pjh':0, 'me':0}

for i in range(len(texts)):
    user = texts[i]['name']
    idx = user.find('-')
    users[user[:idx]] += 1

# parse api results
message = ''
for i in users:
    message += i + ': ' + str(users[i]) + ', '

print(message)
# Send to slack
SLACK_URL = 'https://hooks.slack.com/services/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'
data = {"text":message}
headers = {'Content-type': 'application/json'}

requests.post(SLACK_URL, data=json.dumps(data), headers=headers)