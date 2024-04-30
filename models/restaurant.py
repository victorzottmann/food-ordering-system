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
    if 0 < score <= 5:
      rating = Rating(client, score)
      self._ratings.append(rating)
    
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
    # This is a list comprehension that outputs all the ratings in self._ratings (list), then sum them up
    ratings_sum = sum(rating._score for rating in self._ratings) 
    total_ratings = len(self._ratings)
    avg = round(ratings_sum / total_ratings, 1)
    return avg