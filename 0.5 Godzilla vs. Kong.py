#0.5 Godzilla vs. Kong
budget = float(input())
extras = int(input())
clothing_for_one = float(input())

decor_price = budget * 0.1
clothes_price = extras * clothing_for_one

if extras >= 150:
    clothes_discount = clothes_price * 0.1
    clothes_price -= clothes_discount

film_price = decor_price + clothes_price

if budget >= film_price:
    budget_left = budget - film_price
    print(f"Action!")
    print(f"Wingard starts filming with {budget_left:.2f} leva left.")
else:
    budget_left = film_price - budget
    print(f"Not enough money!")
    print(f"Wingard needs {budget_left:.2f} leva more.")