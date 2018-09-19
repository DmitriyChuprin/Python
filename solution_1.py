'''
1.	Написать класс, перебирающий все числа от 0 до 30, делящиеся на 3, и написать генератор, который умножит эти числа на 2
'''

class Gen:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
                    
    def lst(self):
        return [x for x in range(self.start, self.finish + 1) if x % 3 == 0]
     
    def generatoration(self):
        value = a.lst()
        for i in value:
            yield i * 2


a = Gen(0, 30)
print(a.lst())
b = a.generatoration()
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
