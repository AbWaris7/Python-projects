
print("Earned amount:")
bubblegum = int(input("Bubblegum: "))
toffee = int(input("Toffee: "))
iceCream = int(input("Ice cream: "))
milkChocolate = int(input("Milk chocolate: "))
doughnut = int(input("Doughnut: "))
pancake = int(input("Pancake: "))

income = bubblegum + toffee + iceCream + milkChocolate + doughnut + pancake
print(f"\nIncome: ${income}")

print("Staff expenses:")
staffExpenses = int(input())

print("Other expenses:")
otherExpenses = int(input())

netIncome = income - staffExpenses - otherExpenses
print(f"Net income: ${netIncome}")
