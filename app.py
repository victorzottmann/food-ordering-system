from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.meal import Meal

r_pizza = Restaurant("pizza", "italian")

juice_watermelon = Drink("Watermelon Juice", 5.0, 'large')
r_pizza.add_to_menu(juice_watermelon)

meal_banana_bread = Meal("Banana Bread", 3.50, "Semi-sweet bread made with mashed bananas.")
r_pizza.add_to_menu(meal_banana_bread)

def main() -> None:
    r_pizza.show_menu()

if __name__ == "__main__":
    main()