import re

def read_file():
    with open("iceland.xml","r",encoding="utf-8") as f:
        file=f.readlines()
        return file

def writefile(find_all):
    with open("result.txt","a",encoding="utf-8") as f:
        f.write(find_all + "\n" )

def find_se_inside(text):
    # вводим переменную i, которое при нахождении первой строки с <TEI поменяет значение с 1
    # на -1, и пока программа не дойдет до второй </teiHeader>, программа каждую строку будет
    # добавлять в переменную count. Потом -1*-1=1 и подсчет строк закончится
    i=1
    count=0
    for line in text:
        if re.search("</teiHeader>",line):
            i*=-1
        if i==-1:
            count+=1
        if re.search("<TEI xmlns=",line):
            i*=-1
    return count


# запихала текст ПОЛНОСТЬЮ в функции, исправилась после 10 домашки
def main():
    se=str(find_se_inside(read_file()))
    writefile(se)
    print("Ответ записан.")


main()   
