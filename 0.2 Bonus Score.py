#0.2 Bonus Score
POINTS = int(input())
bonus_points = 0

if POINTS <= 100:
    bonus_points += 5
elif POINTS <= 1000:
    bonus_points += POINTS * 0.2
else:
    bonus_points += POINTS * 0.10

if POINTS % 2 == 0:
    bonus_points += 1
elif POINTS % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(POINTS + bonus_points)