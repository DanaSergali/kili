
import re

def open_file():
    file_name=input("Введите название файла с животным(полностью): ")
    #Коала.html (или вместо коалы: Ушастая аурелия,Фламинго,Лемурообразные,Слоновые)
    if file_name=="":
        print("Вы не ввели название файла.")
        exit(0)
    with open(file_name, encoding="utf-8") as f:
        file=f.read()
    return file


def get_order(text):
    order=re.search(r'>Отряд.*?<a.*?>(.*?)</a>',text)
    order=order.group(1)
    return order


def write_new_file():
    with open("New_file.txt","a",encoding="utf-8") as new_file:
        new=new_file.write(order)



order=get_order(open_file())
write_new_file()

print("Готово. Отряд этого животного записан в New_file. ")

