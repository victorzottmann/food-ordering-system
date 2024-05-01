from models.menu.menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, size) -> None:
        super().__init__(name, price)
        self.size = size
    
    def __str__(self) -> str:
        return self._name