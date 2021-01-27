from main import *
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()
sched.add_job(tags,'interval',seconds=60)

sched.add_job(message,'interval',minutes=2)

sched.add_job(retweet_fun,'interval',hours=8)

sched.add_job(posting,'cron', day_of_week='mon-sun', hour=9)

sched.start()