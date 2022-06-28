# Pizza toppings
toppings = ["pepperoni",
            "pineapple",
            "cheese",
            "sausage",
            "olives",
            "anchovies",
            "mushrooms"]

# Price for each kind of pizza slice
prices = [2,
          6,
          1,
          3,
          2,
          7,
          2]

# Research on $2 slices
num_two_dollar_slices = prices.count(2)

# Length of the topping list
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# 2D list for toppings and their prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"],
                    [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Sorting and Slicing Pizza
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
pricest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "peppers"])
three_cheapest = pizza_and_prices[0:3]

print("Our sorted prices for each topping of pizza are: " + str(pizza_and_prices))
print("Three cheapest pizza are: " + str(three_cheapest))
