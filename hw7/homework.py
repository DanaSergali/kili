filename=input("Введите имя файла: ")

def open_file(txt):
    symbols='!?().,"^"=-'
    with open(txt+".txt","r",encoding = "utf-8") as f:
        text=f.read()
        for symbol in symbols:
            text=text.replace(symbol,"")
        return text.replace("'"," ").split()
    
open_file=open_file(filename)
    
def count_omnis(text):
    count_omnis=[0]
    for word in text:
        if word[:4]=="omni":
            count_omnis[0]+=1
    return count_omnis
count_omnis=count_omnis(open_file)

def count_without_omnis(text):
    count_without_omnis=[0]
    for word in text:
        if word[:4]==" ":
            count_without_omnis[0]+=1
    return count_without_omnis
                
            
count_without_omnis=count_without_omnis(open_file)

print("Количество слов с приставкой omni: ",count_omnis[0])
print("Количество слов без приставки omni: ",count_without_omnis[0])
