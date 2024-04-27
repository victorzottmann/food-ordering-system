from models.restaurant import Restaurant

r_pizza = Restaurant("pizza", "italian")
r_sushi = Restaurant("sushi", "japanese")

r_sushi.toggle_active()

Restaurant.list_restaurants()