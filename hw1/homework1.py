# Variant №3
a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))

if a % b == c: 
    print('YES, первое условие верно')
else:
    print("NOOO, первое условие неверно")

if a*c + b == 0:
    print("YES, Ты прав, второе условие верно")
else:
    print("NOOO, Эх, второе условие неверно")
