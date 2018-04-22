import os

#вторая функция может и не нужна, но я ее добавила, чтобы результат проверить)
def countfile():
    #список файлов и папок там же,где хранится наша программа
    file_list=os.listdir()
    #создаем счетчик для наших названий
    i=0
    symbols=".,:;_()""'\/—«»!?=^|"
    for path in file_list:
        #сплитекстом разбиваем путь на пару dirpath и filename
        dirpath,filename=os.path.splitext(path)
        for letter in dirpath:
            for sy in symbols:
                if sy in letter:
                    i+=1
    print("Всего файлов в директории название которых содержит знаки препинания, было найдено:", i)
                    
    
def writefile():
    file_list=os.listdir()
    #создаем список, в который будем добавлять названия найденных файлов
    sym=[]
    symbols=".,:;_()""'\/—«»!?=^|"
    for path in file_list:
        dirpath,filename=os.path.splitext(path)
        for letter in dirpath:
            for sy in symbols:
                if sy in letter:
                    sym.append(dirpath)
    print("Названия этих файлов(если нужно):", sym)
    
                    
              
def main():
    countfile()
    writefile()
    
    
main()
