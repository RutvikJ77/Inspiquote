from main import *
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()
sched.add_job(tags(api),'interval',minutes=1)

sched.add_job(message(api),'interval',minutes=2)

sched.add_job(retweet_fun(api),'interval',hours=8)

sched.add_job(posting(api),'cron', day_of_week='mon-sun', hour=9)

sched.start()