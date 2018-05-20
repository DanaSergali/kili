import os

def dive():
    #используем функцию walk из новой темы, обходим все папки, начиная с текущего директория(".")
    start_path="."
    #вводим счетчик-калькулятор количества нескольких расширений, их будем добавлять в exp список
    calculate=0
    for root,dirs,files in os.walk(start_path):
        exp=[]
        for names in files:
            #разбиваем путь на пару (root,exp), где exp начинается
            #с точки (расширение) и содержит не более одной точки 
            name,exp1=os.path.splitext(names)
            #это расширение добавляем в список и считаем
            exp.append(exp1)
            if counter(exp)==1:
                calculate+=1
    return calculate

from collections import Counter

#с помощью collections.Counter будем считать количество расширений
def counter(exp):
    expans=Counter(exp)
    #если в нашей паре ключ-значение значение больше или равно 2,
    #то есть расширение встречается несколько раз, мы добавляем эту пару:
    for key, value in expans.items():
        if value>= 2 and key!="":
            return 1

def main():
    calculate=dive()
    print("В ", calculate, " папках встречается несколько файлов с одним и тем же расширением.")

main()
