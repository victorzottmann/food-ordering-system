from models.restaurant import Restaurant

r_pizza = Restaurant("pizza", "italian")
r_pizza.rate("Chico", 5)
r_pizza.rate("Victor", 3)

def main():
    Restaurant.list_restaurants()

if __name__ == "__main__":
    main()