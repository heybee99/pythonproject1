print("*************************************** Welcome to my shopping cart ***************************************")

foods = [] 
prices = [] 
total = 0 

while True:
    food = input("Enter a food to buy (q to quit shopping): ") 
    if food.lower() == "q": 
        break
    else:
        try:
            price = float(input("Enter the price of the food: $")) 
        except ValueError:
            print("Price should be a number")
        else: 
            foods.append(food)
            prices.append(price) 
    

print("*************************************** YOUR CART ***************************************") 

print("Your selected items are ")
for food in foods:
    print(f"{food}", end=" ") 

for price in prices: 
    total += price 

print()
print(f"Your total spending is: ${total}") 