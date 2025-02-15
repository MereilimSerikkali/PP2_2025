import datetime

#Ex1
today = datetime.now()
new_date = today - timedelta(days=5)
print("Date after subtracting 5 days:", new_date.strftime('%Y-%m-%d'))

#Ex2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timdelta(days = 1)
print("yesterday:", yesterday.strftime('%Y-%m-%d'))
print("today:", today.strftime('%Y-%m-%d'))
print("tomorrow:", tomorrow.strftime('%Y-%m-%d'))

#Ex3
now = datetime.now()
print("Original datetime:", now)
without_microseconds = now.replace(microsecond=0)
print("Without microseconds:", without_microseconds)

#Ex4
def date_difference_in_seconds(date1, date2):
    date_format = "%Y-%m-%d %H:%M:%S"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    difference = datetime2 - datetime1
    difference_in_seconds = difference.total_seconds()
    return difference_in_seconds
date1 = "2023-10-01 12:00:00"
date2 = "2023-10-02 12:00:00"
seconds_difference = date_difference_in_seconds(date1, date2)
print(f"The difference between {date1} and {date2} is {seconds_difference} seconds.")
