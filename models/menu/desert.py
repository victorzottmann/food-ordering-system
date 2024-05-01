from models.menu.menu_item import MenuItem

class Desert(MenuItem):
    def __init__(self, name, price, description, category, size) -> None:
        super().__init__(name, price)
        self.description = description
        self.category = category
        self.size = size
    
    def __str__(self) -> str:
        print(self._name)
    
    def apply_discount(self, value):
        if value > 0:
            self._price -= self._price * (value / 100)
        return