import requests, json
from sender.slack import postAlarm
from crontab import CronTab

cron = CronTab(tab="""  * * * * * sender/slack.py""")
