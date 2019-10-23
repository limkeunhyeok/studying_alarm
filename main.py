import schedule, time
from sender.slack import postAlarm

def job():
    postAlarm()

schedule.every().monday.at("09:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)