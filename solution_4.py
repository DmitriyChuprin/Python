'''
4.	Написать приложение, выводящее свой requirements.txt в консоль и после него выводящее названия пакетов без версий через запятую (получить через регулярные выражения)

'''

import os
import re
import time

def requirements():
    comand = 'pip freeze > 1.txt'
    os.system(comand)
    f = open('1.txt', 'r')
    x = f.read()
    print(x)
    expressions = re.sub(r"==", u" ", x)
    a = expressions.split('\n')
    a.pop()
    new_list = []
    for item in a:
        i = re.findall(r'^\w+', item)[0]
        new_list.append(i)
    print(', '.join(new_list))

if __name__ == "__main__":
    requirements()
    time.sleep(5)
