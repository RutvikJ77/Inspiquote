from main import *
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()
sched.add_job(tweet_quote,'interval',hours=6)

sched.add_job(tags,'interval',hours=5)

sched.add_job(message,'interval',hours=4)

sched.add_job(retweet_fun,'interval',hours=24)

sched.add_job(post,'cron', day_of_week='mon-sun',hour=9)

sched.start()