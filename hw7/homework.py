#вариант 6
#я не использую словари, и по-моему решение мое тоже адекватное 
#у других групп отсутствие словарей не влияет на оценку, я надеюсь, и у нас тоже
#я попробую написать еще со словарем тоже
#какова частотность слов с приставкой omni- в тексте и частотность
#слов без приставки omni- (
#то есть, например, сообщает, сколько раз в тексте встречается
#слово omnibenevolent


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
