total_cents = 0
cost = 50

while total_cents < cost:
    coin = int(input("Insert a coin (5, 10, or 25 cents): "))
    
    if coin in [5, 10, 25]:
        total_cents += coin
        remaining = cost - total_cents
        if remaining > 0:
            print("Amount due:", remaining, "cents")
    else:
        print("Invalid coin! Please insert 5, 10, or 25 cents.")

change = total_cents - cost
print("You are owed:", change, "cents in change.")
