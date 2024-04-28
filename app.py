from models.restaurant import Restaurant

r_pizza = Restaurant("pizza", "italian")
r_sushi = Restaurant("sushi", "japanese")
r_sushi.toggle_active()

def main():
  Restaurant.list_restaurants()

if __name__ == "__main__":
  main()