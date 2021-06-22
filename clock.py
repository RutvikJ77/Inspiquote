from apscheduler.schedulers.blocking import BlockingScheduler
from main import tags,tweet_quote,message,post

sched = BlockingScheduler()
sched.add_job(tags, 'interval', hours=5)
sched.add_job(message, 'interval', hours=4)
sched.add_job(tweet_quote, 'interval', hours=12)
sched.add_job(post, 'cron', day_of_week='mon-sun', hour=9)
sched.start()
