'''
2.	Написать программу, которая будет смещать все буквы в фразе на следующую по алфавиту, принимая 
пользовательское значение, состоящее только из букв русского алфавита, из консоли (например собака -> тпвблб)
3.	Добавить к предыдущей программе декоратор, выводящий исходное слово до измененного слова и количество символов в слове после. 

'''
class Example:
    def __init__(self, str):
        self.str = str        

    def shuffle(self):
        new_str = []
        one_str = 'йцукенгшщзхъфывапролджэячсмитьбю'
        alphabet_dict = {
            1: 'а',
            2: 'б',
            3: 'в',
            4: 'г',
            5: 'д',
            6: 'е',
            7: 'ё',
            8: 'ж',
            9: 'з',
            10: 'и',
            11: 'й',
            12: 'к',
            13: 'л',
            14: 'м',
            15: 'н',
            16: 'о',
            17: 'п',
            18: 'р',
            19: 'с',
            20: 'т',
            21: 'у',
            22: 'ф',
            23: 'х',
            24: 'ц',
            25: 'ч',
            26: 'ш',
            27: 'щ',
            28: 'ъ',
            29: 'ы',
            30: 'ь',
            31: 'э',
            32: 'ю',
            33: 'я'}
        for i in self.str:
            if i not in one_str:
                new_str.append(i)
            for key in alphabet_dict.keys():
                if i == 'я':
                    new_str.append('а')
                    break
                else:
                    if alphabet_dict[key] == i:
                        new_str.append(alphabet_dict[key+1])
        new_str = ''.join(new_str)
        return new_str

    def output(func):
        def inner(self):
            length = len(self.shuffle())
            func(self)
            print(f'Length word after shuffle is {length}')
        return inner

    @output
    def name(self):
        print(f'First name is {self.str}')



   
a = Example('собака')
print(a.shuffle())
a.name()

