import requests, json


# commit 메시지 파싱
def messageParsing(message):
    res = []
    temp = message
    while True:
        # '-'가 없다면 종료
        if temp.find('-') == -1:
            return res
        # commit 메시지에서 처음 발견되는 '-'를 보고 파싱한뒤, 슬라이싱 후에 다시 반복
        else:
            index = temp.find('-')
            res.append(temp[index + 1: index + 4])
            temp = temp[index + 4:]
            continue


# commit이 중복되는지 체크
def checkCommit(user, commit):
    temp = list(user.keys())
    # key 리스트에 있다면 True, 없으면 False
    if commit in temp:
        return True
    else:
        return False

# Get Branch data from github
branch_name = ['keunhak', 'keunhyeok', 'ksbyun']
GITHUB_URL_Prefix = 'https://api.github.com/repos/limkeunhyeok/algorithm-study/commits?sha='
users = {'keunhak':{}, 'keunhyeok':{}, 'ksbyun':{}}

for name in branch_name:
    apiResults = requests.get(GITHUB_URL_Prefix + name)
    texts = apiResults.json()
    for i in range(len(texts) - 5):
        commit = texts[i]['commit']['message']
        commit = messageParsing(commit)
        for j in commit:
            chapter = j[0]
            problem = j[2]
            if checkCommit(users[name], chapter):
                if checkCommit(users[name][chapter], problem):
                    continue
                else:
                    users[name][chapter][problem] = texts[i]['sha']
            else:
                users[name][j[0]] = {j[2]: texts[i]['sha']}

nick = {'keunhak':'임근학(KeunHak)', 'keunhyeok':'임근혁(KeunHyeok)', 'ksbyun':'변기석(KiSeok)'}
message = ''
for user in users:
    message += nick[user] + '님\n'
    for chapter in users[user]:
        message += 'chapter' + chapter + '\n'
        sortProb = sorted(users[user][chapter].keys())
        for problem in sortProb:
            message += '문제 {0}. URL: https://github.com/limkeunhyeok/algorithm-study/commit/{1}\n'.format(problem, users[user][chapter][problem])
    message += '----------------------------\n'


temp = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "최근 등록된 알고리즘은 총 n개이며 임근학님 n1개, 변기석님 n2개, 박주현님 n3개, 임혜성님 n4개, 임근혁님 n5개 입니다. \n\n*알고리즘 풀이 내역*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*임근학(keunhak)* 님은 총 n1개의 문제를 푸셨습니다."
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-0>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-1>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-2>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-3>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-1>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-2>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-3>"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*변기석(ksbyun)* 님은 총 n2개의 문제를 푸셨습니다."
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-0>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-2>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-3>"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*임근혁(ksbyun)* 님은 총 n2개의 문제를 푸셨습니다."
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-0>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-2>"
				}

			]
		},
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*임근혁(ksbyun)* 님은 총 n2개의 문제를 푸셨습니다."
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-0>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-2>"
				}

			]
		},
            {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*임근혁(ksbyun)* 님은 총 n2개의 문제를 푸셨습니다."
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-0>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-2>"
				}

			]
		},
            {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*임근혁(ksbyun)* 님은 총 n2개의 문제를 푸셨습니다."
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-6-0>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://github.com/limkeunhyeok/algorithm-study/commit/192e73e4a745ce2c7cc585e18b5e33714375669a|lkh-7-2>"
				}

			]
		},
		{
			"type": "divider"
		}
	]
}
