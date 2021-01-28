from main import *
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()
sched.add_job(tags,'interval',minutes=3)

sched.add_job(message,'interval',minutes=4)

sched.add_job(retweet_fun,'interval',hours=8)

sched.add_job(post,'cron', day_of_week='mon-sun', hour=16,minute=20)

sched.start()