from models.menu.menu_item import MenuItem

class Meal(MenuItem):
    def __init__(self, name, price, description) -> None:
        super().__init__(name, price)
        self.description = description
    
    def __str__(self) -> str:
        return self._name