#0.4 Toy Shop
#Toy Prices:
PUZZLE = 2.60
TALKING_DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TOY_TRUCK = 2

DISCOUNT = 25 / 100 # 25% if the purchase exceeds 50 products
RENT = 10 / 100 # 10% For rent

excursion_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = puzzle_count * PUZZLE
doll_price = doll_count * TALKING_DOLL
bear_price = bear_count * TEDDY_BEAR
minion_price = minions_count * MINION
truck_price = trucks_count * TOY_TRUCK

toy_count = puzzle_count + doll_count + bear_count + minions_count + trucks_count
toy_sum = puzzle_price + doll_price + bear_price + minion_price + truck_price

if toy_count >= 50:
    discount = toy_sum * DISCOUNT
else:
    discount = 0

end_sum = toy_sum - discount
rent = end_sum * RENT
profit = end_sum - rent

if profit >= excursion_price:
    profit -= excursion_price
    print(f"Yes! {profit:.2f} lv left.")
else:
    loss = excursion_price - profit
    print(f"Not enough money! {loss:.2f} lv needed.")