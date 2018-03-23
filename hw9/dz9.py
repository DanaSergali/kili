import re

with open("kenner.txt","r",encoding="utf-8") as f:
    text=f.read().lower().replace("\n"," ")
    download=[]
    participium=download.append(str(re.findall("[Зз]агруженн[а-я]*[^\s]", text)))
    gerund=download.append(str(re.findall("[Зз]агружа[яв]", text)))
    infinitive=download.append(str(re.findall("[Зз]агру[жз][иа]ть[а-я]*[^\s,.!?:;]", text)))
    prost=download.append(str(re.findall("[Зз]агру[жз][а-я]*[^\s,.!?:;]", text)))
    self=download.append(str(re.findall("[Зз]агру[жз][а-я]*[^\s,.!?:;]ся", text)))
    
if download:
    print("Найденные формы глагола Загрузить: ", download)
else:
    print("Ничего не найдено")
      
