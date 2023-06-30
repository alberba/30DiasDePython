from datetime import *

# Get the current day, month, year, hour, minute and timestamp from datetime module
date_now = datetime.now()

print("Day:",date_now.day)
print("Month:",date_now.month)
print("Year:",date_now.year)
print("Hour:",date_now.hour)
print("Minute:",date_now.minute)
print("Timestamp:",date_now.timestamp())
print(date_now.strftime("%m/%d/%Y, %H:%M:%S"))

# Today is 5 December, 2019. Change this time string to time.
today = "5 December, 2019"
print(datetime.strptime(today, "%d %B, %Y"))

# Calculate the time difference between now and new year.
new_year = datetime(year = 2024, month = 1, day = 1)
print("Time left for new year:", new_year - date_now)

# Calculate the time difference between 1 January 1970 and now.
old = datetime(year = 1970, month = 1, day = 1)
print(date_now - old)