from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.meal import Meal

r_pizza = Restaurant("pizza", "italian")

juice_watermelon = Drink("Watermelon Juice", 5.0, 'large')
juice_watermelon.apply_discount(5)

meal_banana_bread = Meal("Banana Bread", 3.50, "Semi-sweet bread made with mashed bananas.")
meal_banana_bread.apply_discount(8)

r_pizza.add_to_menu(juice_watermelon)
r_pizza.add_to_menu(meal_banana_bread)

def main() -> None:
    r_pizza.show_menu()

if __name__ == "__main__":
    main()