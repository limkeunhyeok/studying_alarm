from collector.github import commitCount, getUsersCommit

# 메세지 포맷팅
def messageFormatting():
    users = getUsersCommit()
    count = commitCount(users)
    message = {
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
                        }
                    ]
                },
                {
                    "type": "divider"
                }
            ]
        }
    return message
print(messageFormatting())