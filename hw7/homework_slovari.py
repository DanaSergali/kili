print("Приставки OMNI: ")
    
def read(txt):
    symbols='!?().,"^"=-'
    with open(txt, encoding="utf-8") as f:
        text = f.read()
        for symbol in symbols:
            text=text.replace(symbol,"")
            text=text.replace("'"," ")
            text=text.lower()
            words=text.split()
        return words
    



def count_omnis(words):
    omni={}
    for word in words:
        if word[:4]=="omni":
            if word in omni:
                omni[word]+=1
            else:
                omni[word]=1
    return omni 


def count_without_omni(words,omni):
    without={}
    for word in omni:
        if word[4:] in words:
                for s in words:
                    if s==word[4:]:
                        if s in without:
                            without[s]+=1
                        else:
                            without[s]=1
    return without

    

def frequency(dic):
    for word, summ in dic.items():
        print(word,":",summ)
    if len(dic)==0:
        print("Таких слов нет.")



def main():
    omni= count_omnis(read("text.txt"))
    without = count_without_omni(read("text.txt"),omni)  
    print("Количество слов с приставкой omni: ",frequency(omni))
    print("Количество слов без приставки omni: ",frequency(omni))

main()
