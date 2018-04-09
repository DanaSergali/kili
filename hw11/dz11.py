import re

def read_file():
    #у меня браузер чуть гонит и не хочет сохранять страницу в html, я сохранила
    #код страницы в кодировке utf-8 
    with open("Finland.txt", encoding="utf-8") as f:
        file=f.read()
    return file

def lines_all(new_text):
    new_text=re.sub(r'Финляндия\b','Малайзия',new_text)
    #конечно, вряд ли в Википедии встретится название страны с маленькой буквы, но в задании было
    #уточнение про маленькую и большую букву, поэтому вот 
    new_text=re.sub(r'финляндия','малайзия',new_text)
    new_text=re.sub(r'Независимая_Финляндия_','Независимая_Малайзия_',new_text)
    new_text=re.sub(r'Финляндией','Малайзией',new_text)
    new_text=re.sub(r'Финляндии','Малайзии',new_text)
    new_text=re.sub(r'Финляндию','Малайзию',new_text)    
    return new_text

def writefile(new_text):
    with open("result.txt","w",encoding="utf-8") as f:
        f.write(new_text)


def main():    
    writefile(lines_all(read_file()))

main()
