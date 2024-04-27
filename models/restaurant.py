class Restaurant:
  def __init__(self, name, category, active = False):
    self.name = name
    self.category = category
    self.active = active
  
  def __str__(self):
    return f"Name: {self.name}, Category: {self.category}, Active: {self.active}"