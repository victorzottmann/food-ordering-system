class Restaurant:
  restaurants = []
  
  def __init__(self, name, category, active = False) -> None:
    self.name = name
    self.category = category
    self.active = active
    Restaurant.restaurants.append(self)
  
  def __str__(self) -> str:
    return f"Name: {self.name}, Category: {self.category}, Active: {self.active}"
  
  def list_restaurants() -> None:
    for r in Restaurant.restaurants:
      print(f"Name: {r.name}, Category: {r.category}, Active: {r.active}")