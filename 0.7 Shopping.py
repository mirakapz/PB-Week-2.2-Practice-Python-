#0.7 Shopping
GPU = 250

budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = gpu_count * GPU
cpu_price = cpu_count * (gpu_price * 0.35)
ram_price = ram_count * (gpu_price * 0.1)

total_price = gpu_price + cpu_price + ram_price
sum = total_price

if gpu_count > cpu_count:
    sum = total_price - (total_price * 0.15)

if sum <= budget:
    balance = budget - sum
    print(f"You have {balance:.2f} leva left!")
else:
    balance = sum - budget
    print(f"Not enough money! You need {balance:.2f} leva more!")