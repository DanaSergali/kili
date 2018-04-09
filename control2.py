#исправилась после 10 домашки и абсолютно все запихала в функции
import re
def get_text():
    with open('iceland.xml',"r", encoding='utf-8') as f:
        file=f.read()
    return file

def matches(text):
    c=re.match(r'.*</teiHeader>',text, re.DOTALL)
    return c

def lines_all(c):
    c=c.splitlines()
    i=0
    for line in c:
        i+= 1
    return i

def write(i):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("1 задание"+"\n"+i)


def main():
    c=matches(get_text()).group()
    i=str(lines_all(c))
    write(i)

main()
