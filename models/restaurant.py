from models.rating import Rating

class Restaurant:
  restaurants = []
  
  def __init__(self, name, category, active = False) -> None:
    self._name = name.capitalize()
    self._category = category.capitalize()
    self._active = active
    self._ratings = []
    Restaurant.restaurants.append(self)
  
  def __str__(self) -> str:
    return f"Name: {self._name}, Category: {self._category}, Active: {self._active}"
  
  def toggle_active(self):
    self._active = not self._active
    
  def rate(self, client, score):
    grade = Rating(client, score)
    self._ratings.append(grade)
    
  @classmethod
  def list_restaurants(cls) -> None:
    print(f"{'Name'.ljust(25)} | {'Category'.ljust(25)} | Status")
    for r in cls.restaurants:
      print(f"{r._name.ljust(25)} | {r._category.ljust(25)} | {r._active}")

  @property
  def active(self):
    return "Active" if self._active else "Inactive"