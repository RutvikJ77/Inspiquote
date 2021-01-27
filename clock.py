from main import *
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()
sched.add_job(tags(api),'interval',seconds=5)

sched.add_job(message(api),'interval',minutes=2)

sched.add_job(retweet_fun(api),'interval',hour=8)

sched.add_job(posting(api),'cron', day_of_week='mon-sun', hour=9)

sched.start()