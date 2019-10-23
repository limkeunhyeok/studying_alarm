import os, requests, json
from formatter.formatting import alarmForm
# 알고리즘 풀이 내역 slack으로 보내기
def postAlarm():
    message = alarmForm()
    SLACK_URL = 'https://hooks.slack.com/services/' + os.environ['SLACK_KEY']
    headers = {'Content-type': 'application/json'}
    requests.post(SLACK_URL, data=json.dumps(message), headers=headers)

postAlarm()