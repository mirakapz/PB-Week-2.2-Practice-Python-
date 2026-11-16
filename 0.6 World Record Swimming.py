#0.6 World Record Swimming
from math import floor

record_sec = float(input())
distance_m = float(input())
time_meter_swam = float(input())

goal = distance_m * time_meter_swam

extorted_time = floor(distance_m / 15) * 12.5
total_time = goal + extorted_time

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    time_loss = total_time - record_sec
    print(f"No, he failed! He was {time_loss:.2f} seconds slower.")