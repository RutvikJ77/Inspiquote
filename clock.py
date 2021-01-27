from main import *
from apscheduler.schedulers.blocking import BlockingScheduler

@sched.scheduled_job('interval',seconds=5)
def timed_job_tags():
    tags(api)

@sched.scheduled_job('interval',minutes=2)
def timed_job_follow():
    message(api)

@sched.scheduled_job('interval',hour=8)
def timed_job_retweet():
    retweet_fun(api)

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=9)
def scheduled_job():
    posting(api)

sched.start()