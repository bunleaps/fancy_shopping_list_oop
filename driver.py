from shopping import FancyShoppingListBS


def food_data_BS():
    food = list()
    num_of_items = int(input("How many items will you order today? "))

    while num_of_items <= 0:
        print("Number of items must be at least 1.")
        num_of_items = int(input("How many items will you order today? "))

    for i in range(num_of_items):
        print(f"\nItem #{i + 1} - ")
        food_name = input("Enter Food: ")
        food_amount = float(input("Enter amount of pounds: "))

        while food_amount <= 0:
            print("Amount of pounds must be at least 1.")
            food_amount = float(input("Enter amount of pounds: "))

        food.append({food_name: food_amount})

    return food


def display_content_BS(data):
    print("\nHere's a summary of the items purchased:")
    print("-------------------------------")

    for i in data:
        for a, b in i.items():
            item = FancyShoppingListBS(a, b)
            price = item.CalculateCostBS()
            print(f"Item: {a}")
            print(f"Amount ordered: {b} pounds")
            print(f"Price per pound: ${item.getPricePerPoundBS():.2f}")
            print(f"Price of order: ${price:.2f} \n")


def total_cost_BS(data):
    total = 0

    for i in data:
        for a, b in i.items():
            item = FancyShoppingListBS(a, b)
            price = item.CalculateCostBS()
            total += price

    print(f"Total cost: ${total:.2f}")


def main():
    food_list = food_data_BS()
    display_content_BS(food_list)
    total_cost_BS(food_list)


main()
