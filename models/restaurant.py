from models.rating import Rating
from models.menu.menu_item import MenuItem

class Restaurant:
    restaurants = []
  
    def __init__(self, name, category, active = False) -> None:
        self._name = name.capitalize()
        self._category = category.capitalize()
        self._active = active
        self._ratings = []
        self._menu = []
        Restaurant.restaurants.append(self)
  
    def __str__(self) -> str:
        return f"Name: {self._name}, Category: {self._category}, Active: {self._active}"
    
    def toggle_active(self) -> None:
        self._active = not self._active
        
    def rate(self, client, score) -> None:
        if 0 < score <= 5:
            rating = Rating(client, score)
            self._ratings.append(rating)
    
    def add_to_menu(self, item) -> None:
        """
        Since Meal and Drink are derived from MenuItem, it is ideal to have a single method
        responsible for adding items to the restaurant's menu, regardless of what category
        they belong to.
        
        For example, isinstance(item, MenuItem) checks whether the item is an instance of the MenuItem class.
        If so, only then append the item to the menu.
        
        Here, meals and drinks are instances of MenuItem because Drink inherits from MenuItem.
        """
        if isinstance(item, MenuItem):
            self._menu.append(item)
    
    def show_menu(self) -> None:
        print(f"\nRestaurant {self._name} - Menu")
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item, "description"):
                message_meal = f"{i}. {item._name.ljust(17)} | ${item._price:.2f} | Description: {item.description}"
                print(message_meal)
            else:
                message_drink = f"{i}. {item._name.ljust(17)} | ${item._price:.2f} | Size: {item.size}"
                print(message_drink)
  
    @classmethod
    def list_restaurants(cls) -> None:
        print(f"{'Name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(25)} | Status")
        for r in cls.restaurants:
            print(f"{r._name.ljust(25)} | {r._category.ljust(25)} | {str(r.get_average_rating).ljust(25)} | {r._active}")

    @property
    def active(self) -> str:
        return "Active" if self._active else "Inactive"
    
    @property
    def get_average_rating(self) -> float:
        if not self._ratings:
            return '-'
        # This is a list comprehension that outputs all the ratings in self._ratings (list), then sums them up
        ratings_sum = sum(rating._score for rating in self._ratings) 
        total_ratings = len(self._ratings)
        avg = round(ratings_sum / total_ratings, 1)
        return avg