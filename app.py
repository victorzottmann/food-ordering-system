from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.meal import Meal

r_pizza = Restaurant("pizza", "italian")
juice_watermelon = Drink("Watermelon Juice", 5.0, 'Large')
meal_banana_bread = Meal("Banana Bread", 3.50, "Semi-sweet bread made with mashed bananas.")

def main() -> None:
    print(juice_watermelon)
    print(meal_banana_bread)

if __name__ == "__main__":
    main()