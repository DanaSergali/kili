d=0
s=0
while True:
    print("Введите число: ")
    y=input()
    if y=="":
        break
    y=float(y)
    d += 1
    s += y
    

    if d==1:
        maximum=y
        minimum=y
    else:
        if y>maximum:
            maximum=y
        if y<minimum:
            minimum=y

if d==0:
    print("Вы ничего не ввели.")
else:   
    print("Максимальное введенное число: ", maximum)
    print("Минимальное введенное число: ", minimum)
    print("Среднее арифметическое введенных чисел: ",s/d)
