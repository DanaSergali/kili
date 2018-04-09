import re

def read_file(file):
  with open (file,"r",encoding="utf-8'") as f:
    text=f.read()
  return text


import collections

def lines_all(file):
    c=re.findall('w lemma=".*?" type="(.*?)"',file)
    #добавим словарь Counter
    #каунтер из модуля коллекции
    #инфу нашла на pythonworld
    c=collections.Counter(c)
    # в тот же самый файл в который мы писали первое задание,
    # добавляем пары ключ-значение
    with open ("result.txt","a",encoding="utf-8'") as f:
        #данные сортируем по длине строки, но в обратном порядке(разворачиваем
        #очередь) хабрахабр
        for key in sorted(c,key=c.get,reverse=True):
            res="\n"+key+" "+str(c[key])
            f.write(res) 
      
      

def main():
  lines_all(read_file('Iceland.xml'))
  print("Ответ записан.")

main()
