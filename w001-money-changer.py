# Code Crafter Weekly Challenges
# Week 01 - Money Change Problem
# Compute the minimum number of coins needed to change the given value into coins with denominations 1, 5, and 10.
# Author: Pramod Lakshan - BSE 2023/24

def money_changer(amount):
    initial_amount = amount
    coins = [10, 5, 1]
    change = []
    temp_change = 0
    count = 0
    for coin in coins:
        temp_change = amount // coin
        if temp_change != 0:
            for i in range(temp_change):
                change.append(coin)
            count += temp_change
        amount %= coin
    print(f"\nTotal coins: {count}")
    print(f"Coins used to change {initial_amount}:", ",".join(map(str, change)), "\n")

amount = int(input("\nEnter the amount you want to change: "))
if amount < 1 or amount > 1000:
    print("\nPlease enter an amount between 1 and 1000.\n")
else:
    money_changer(amount)
