'''
5. Реализовать класс Fruit с переменными size, weight(числовые значения) и
taste(строковое), отнаследовать от него классы apple с новой переменной 
color(строковое значение) и orange с переменной color, но без taste. 
Положить два яблока и апельсин в FruitBasket.
'''
class Fruit:
    def __init__(self, size: int, weight: int, taste: str):
        self.size = size
        self.weight = weight
        self.taste = taste
        self.name = self.__class__.__name__
    
    def __repr__(self):
        return f'This is a/an {self.name}.' 

class Apple(Fruit):
    def __init__(self, color, size, weight):
        self.color = color
        Fruit.__init__(self, size, weight, taste = '')
    
    

class Orange(Fruit):
    def __init__(self, color, size, weight):
        self.color = color
        Fruit.__init__(self, size, weight, taste = '')

class Fruitbasket:
    def __init__(self, size, volume = []):
        self.size = size
        self.volume = volume

    def get_fruit(self, smth):
        self.volume.append(smth)
        return self.volume


apple = Apple('red', 15, 0.5)
orange = Orange('orange', 10, 0.3)
basket = Fruitbasket(100)
basket.get_fruit(apple)
basket.get_fruit(apple)
basket.get_fruit(orange)
print(basket.volume)


