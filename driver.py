from shopping import FancyShoppingListBS


# a function to return food list()
def food_data_BS():
    # initialize food list
    food = list()
    # number of items prompt
    num_of_items = int(input("How many items will you order today? "))

    # validation on num of items
    # make sure it is bigger than 0
    while num_of_items <= 0:
        print("Number of items must be at least 1.")
        num_of_items = int(input("How many items will you order today? "))

    # if number of items is valid
    # ask for food name and amount in pounds
    for i in range(num_of_items):
        print(f"\nItem #{i + 1} - ")
        food_name = input("Enter Food: ")
        food_amount = float(input("Enter amount of pounds: "))

        # validation on food amount
        # make sure it is bigger than 0
        while food_amount <= 0:
            print("Amount of pounds must be at least 1.")
            food_amount = float(input("Enter amount of pounds: "))

        # append the information from user
        # to the main food list
        food.append({food_name: food_amount})

    # return food list for later use
    return food


# function to display food list content
def display_content_BS(data):
    print("\nHere's a summary of the items purchased:")
    print("-------------------------------")

    # loop through food list
    # to get each dictionary
    for i in data:
        # in the dict
        # loop to get keys and values
        for a, b in i.items():
            # initialize the shopping module
            # with a(food name) and b(amount in pounds)
            item = FancyShoppingListBS(a, b)
            price = item.CalculateCostBS()

            # print the content
            print(f"Item: {a}")
            print(f"Amount ordered: {b} pounds")
            print(f"Price per pound: ${item.getPricePerPoundBS():.2f}")
            print(f"Price of order: ${price:.2f} \n")


# calculate the total cost of all items
def total_cost_BS(data):
    # initialize the total
    total = 0

    # loop through food list
    # to get each dictionary
    for i in data:
        # in the dict
        # loop to get keys and values
        for a, b in i.items():
            # initialize the shopping module
            # with a(food name) and b(amount in pounds)
            item = FancyShoppingListBS(a, b)
            # get price of the item
            price = item.CalculateCostBS()
            # add the item total price to overall total price
            total += price

    # print total price
    print(f"Total cost: ${total:.2f}")


# main function program
def main():
    # assign food_list with the food items list
    food_list = food_data_BS()
    # display the content using the food_list list
    display_content_BS(food_list)
    # calculate and display total using the food_list list
    total_cost_BS(food_list)


# run program
main()
