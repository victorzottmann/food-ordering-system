from models.menu.menu_item import MenuItem

class Meal(MenuItem):
    def __init__(self, name, price, description) -> None:
        super().__init__(name, price)
        self.description = description
    
    def __str__(self) -> str:
        return self._name
    
    def apply_discount(self, value) -> None:
        if value > 0:
            self._price -= self._price * (value / 100)
        return