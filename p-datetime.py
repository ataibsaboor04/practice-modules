import datetime as dt
import time as tm

"CURRENT DATE AND TIME"

# time returns the current time in seconds since the Epoch. (January 1st, 1970)
tm.time()

# conver the timestamp to datetime
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow

# or simply
dt.datetime.today()

# if you want only date
dt.date.today()

dtnow = dt.datetime.today()
# datetime attributes
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
# get year, month, day, etc.from a datetime

# get the day
dtnow.weekday()  # Monday - 0, Sunday - 6

# or
dtnow.isoweekday()  # Monday - 1, Sunday - 67

today = dt.datetime.today()
today

now = dt.datetime.now()
now

utcnow = dt.datetime.utcnow()
utcnow

"TIME DELTA"

# create a timedelta of 100 days
delta = dt.timedelta(days=100)
delta

# the date 100 days ago
today - delta

# compare the dates
today > today-delta

"MAKING DATES"

dt.date(2020, 3, 18)  # year, month, day

dt.time(4, 39, 23, 283200)  # hour, minute, second, millisecond

# year, month, day, hour, minute, second, millisecond
dt.datetime(2018, 8, 29, 3, 12, 40, 9000)

date = dt.datetime(2018, 8, 29, 3, 12, 40, 9000)
date.time(), date.date()  # attributes
