from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price
    
    @abstractmethod
    def apply_discount(self):
        pass