from collector.github import getCommitCount, getUsersCommit
import copy

# 알고리즘 풀이 내역 form
def alarmForm():
    userCommitCount = getCommitCount(getUsersCommit())
    username = {'keunhak': '임근학', 'ksbyun': '변기석', 'keunhyeok': '임근혁', 'juhyeon': '박주현', 'hyeseong': '임혜성'}
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "현재 등록된 알고리즘은 총 {}개 입니다.\n*<https://github.com/limkeunhyeok/algorithm-study|github - algorithm_study>*".format(
                        userCommitCount['total'])
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": []
            }
        ]
    }
    fields = {
        "type": "mrkdwn",
        "text": ""
    }
    for user in username:
        if user in userCommitCount:
            temp = copy.deepcopy(fields)
            temp["text"] = "*{0}({1}):*\n알고리즘 {2}개 풀이".format(username[user], user, userCommitCount[user])
            message["blocks"][2]["fields"].append(temp)
        else:
            temp = copy.deepcopy(fields)
            temp["text"] = "*{0}({1}):*\n알고리즘 {2}개 풀이".format(username[user], user, str(0))
            message["blocks"][2]["fields"].append(temp)
    return message

'''
# 메세지 포맷팅, 추후 bot을 이용해 활용예정
def userCommitForm():
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ""
                }
            },
            {
                "type": "divider"
            }
        ]
    }

    username = {'keunhak': '임근학', 'ksbyun': '변기석', 'keunhyeok': '임근혁'} 
    usercommit = getUsersCommit()
    usercount = getCommitCount(usercommit)

    introText = '현재 등록된 알고리즘은 총 {}개이며'.format(usercount['total'])
    for key in usercount:
        if key == 'total':
            introText += ' 입니다. \n\n*알고리즘 풀이 내역*'
        else:
            introText += ', ' + username[key] + '님 ' + str(usercount[key]) + '개'

    message['blocks'][0]['text']['text'] = introText

    userCommitText = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ""
        }
    }

    userCommitURL = {
        "type": "section",
        "fields": []
    }

    fields = {
        "type": "mrkdwn",
        "text": ""
    }

    for name in username:
        userCommitText['text']['text'] = "*{0}({1})* 님은 총 {2}개의 문제를 푸셨습니다.".format(username[name], name,
                                                                                   usercount[name])
        tempText = copy.deepcopy(userCommitText)
        message['blocks'].append(tempText)
        message['blocks'].append(userCommitURL)
        for key in usercommit[name]:
            fields['text'] = "<{0}|{1}>".format(usercommit[name][key], key)
            tempFields = copy.deepcopy(fields)
            userCommitURL['fields'].append(tempFields)
            tempURL = copy.deepcopy(userCommitURL)
        message['blocks'].append(tempURL)
    return message
'''