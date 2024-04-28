from models.restaurant import Restaurant

r_pizza = Restaurant("pizza", "italian")
r_pizza.rate("Victor", 8)
r_pizza.rate("Claude", 7.5)
r_pizza.rate("Chico", 10)

def main():
  Restaurant.list_restaurants()

if __name__ == "__main__":
  main()