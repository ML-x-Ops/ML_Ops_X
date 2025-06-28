class Pizza:
    def __init__(self, size, suace, meat, toppings):
        pass

class PizzaBaker:
    def __init__(self):
        self._size = ""
        self._sauce = []
        self._meat = ""
        self._toppings = []
    
    def tell_size(self, size):
        self._size = size
        return self
    
    def add_sauce(self, sauce):
        self._sauce.append(sauce)
        return self
    
    def meat_name(self, meat):
        self._meat = meat
        return self

    def add_toppings(self, toppings):
        self._toppings.append(toppings)
        return self
    
    def bake(self):
        return Pizza(
            self._size,
            self._sauce,
            self._meat,
            self._toppings)
    
pizza = (PizzaBaker()
        .tell_size("Large")
        .add_sauce("tomato")
        .add_toppings("cheese")
        .add_toppings("olives")
        .add_sauce("chilli")
        .add_toppings("chilli flakes")
        .bake())