import requests
from formatter.message import getKey, messageParsing, checkCommit

# 브랜치 이름 가져오기
def getBranchName():
    branch_name = []
    apiResults = requests.get('https://api.github.com/repos/limkeunhyeok/algorithm-study/branches')
    texts = apiResults.json()
    for i in range(len(texts)):
        if texts[i]['name'] == 'master':
            continue
        else:
            branch_name.append(texts[i]['name'])
    return branch_name

# 사용자별 commit 가져오기
def getUsersCommit():
    branch_name = getBranchName()
    GITHUB_URL_Prefix = 'https://api.github.com/repos/limkeunhyeok/algorithm-study/commits?sha='
    users = {}
    users_keys = getKey()
    for i in branch_name:
        users[i] = {}

    for name in branch_name:
        apiResults = requests.get(GITHUB_URL_Prefix + name)
        texts = apiResults.json()
        for index in range(len(texts) - 5):
            commits = texts[index]['commit']['message']
            commits = messageParsing(commits, users_keys[name])
            for commit in commits:
                if checkCommit(users[name], commit):
                    continue
                else:
                    users[name][commit] = texts[index]['html_url']
    return users

# 사용자별 commit 수
def getCommitCount(users):
    count = {}
    totalCount = 0
    for user in users:
        count[user] = len(users[user])
        totalCount += len(users[user])
    count['total'] = totalCount
    return count