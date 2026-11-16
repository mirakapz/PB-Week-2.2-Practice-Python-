#0.3 Time + 15 Minutes
TIME_MINUTES = 60
TIME_HOUR = 24

hour = int(input())
minutes = int(input())

minutes += 15

if minutes >= TIME_MINUTES:
    hour += 1
    minutes -= TIME_MINUTES

if hour >= TIME_HOUR:
    hour %= TIME_HOUR

print(f"{hour}:{minutes:02d}")
