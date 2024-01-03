coins = 0
cost = 50

while coins < cost:
    print(f"Amount Due: {cost - coins}")
    c = input("Insert Coin: ")
    if c == "5" or c == "10" or c == "25":
        coins = coins + int(c)

print(f"Change Owed: {coins - cost}")
