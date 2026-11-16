#0.8 Lunch Break
from math import ceil

serial_name = input()
episode_length = int(input())
break_length = int(input())

lunch_break = break_length / 8
breather_time = break_length / 4
rest_time = (break_length - lunch_break - breather_time)

if episode_length <= rest_time:
    time_left = ceil(rest_time - episode_length)
    print(f"You have enough time to watch {serial_name} and left with {time_left} minutes free time.")
else:
    time_left = ceil(episode_length - rest_time)
    print(f"You don't have enough time to watch {serial_name}, you need {time_left} more minutes.")