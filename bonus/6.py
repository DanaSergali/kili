v = int(input("Введите свой вес в килограммах: "))
r = int(input("Введите свой рост в сантиметрах: "))

IMT=v/((r/100)**2)
print("Индекс массы тела равен ",round(IMT,2))
#round - округляем введенное число
print("Что у вас: ")

if IMT <= 16:
    print("Выраженный дефицит массы тела => Вы слишком худой")
elif (IMT>16) and (IMT<=18.5):
    print("Недостаточная (дефицит) масса тела => Вы худовастенький")
elif (IMT>18.5) and (IMT<=24.99):
    print("У вас нормальный вес, норма")
elif (IMT>=25) and (IMT<=30):
    print("У вас есть избыточная масса тела => Надо чуть-чуть похудеть")
elif (IMT>30) and (IMT<= 35):
    print("У вас ожирение I степени......")
elif (IMT>35) and (IMT<= 40):
    print("У вас ожирение II степени.........")
else:
    print("У вас жирение III степени (морбидное):CC......Все плохо..")
