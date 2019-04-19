import datetime
x=datetime.datetime.today()
previous_time=x-datetime.timedelta(days=1)
previous_time1=previous_time-datetime.timedelta(days=1)
print x
print previous_time
print previous_time1
