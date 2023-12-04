class FancyShoppingListBS:
    # Initial Private Variables
    def __init__(self, name, amount):
        self.__food_name = name
        self.__food_amount = amount
        self.__standard_price = 0.00
        self.__total_price = 0

    # Check the food name and set the standard price
    # which is the price per pound
    def __PriceListBS(self):
        self.__food_items = {
            "Dry Cured Iberian Ham": 177.80,
            "Wagyu Steaks": 450.00,
            "Matsutake Mushrooms": 272.00,
            "Kopi Luwak Coffee": 306.50,
            "Moose Cheese": 487.20,
            "White Truffles": 3600.00,
            "Blue Fin Tuna": 3603.00,
            "Le Bonnotte Potatoes": 270.81,
        }

        # Loop the food items dict and set the standard price
        if self.__food_name in self.__food_items:
            self.__standard_price = self.__food_items[self.__food_name]
        else:
            # if item is not in the dict
            # get the price to 0.00
            self.__standard_price = 0.00

    # Accessor to get the Price Per Pound
    def getPricePerPoundBS(self):
        return self.__standard_price

    # Calculate the cost of an item by
    # Food Amount * Price per Pound
    def CalculateCostBS(self):
        self.__PriceListBS()
        self.__total_price = self.__food_amount * self.__standard_price
        return self.__total_price
