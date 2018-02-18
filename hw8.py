import random
print("Поиграем. Я загадала слово. Попробуй угадай.")
print("Я буду давать подсказки")

#создаем словарь с нашими словами и подсказками,
#каждому загаданному слову прикрепляем список из подсказок
#у меня с csv файлом на компе заморочки с экселем,
#и знаки табуляции воспринимались программой нерправильно,поэтому txt, извини :((
def dictionary():
    with open("strana.txt",encoding="utf-8") as f:
        enigma={}
        for words in f:
            enig,e1,e2,e3=words.split(",",maxsplit=3)
            put_inside=enigma.setdefault(enig,[])
            put_inside.append(e1)
            put_inside.append(e2)
            put_inside.append(e3)
    return enigma



def game(enigma):
    #Сортируем наши загаданные слова и программа рандомно вытягивает одно из них
    wordlist=sorted(enigma.keys())
    word=random.choice(wordlist)
    print("Я загадала страну. В подсказках \
будут столица, стереотипы или язык, на котором там говорят. ")
    print("Загаданные страны находятся в Европе, Латинской Америке и Азии.\
Попробуй введи любую.") 
    d=0
    #Пользователь вводит предположение, ввод пустой строки предусмотрен
    tries=input()
    hint=random.choice(enigma[word])
    while tries!=word:
        if tries=="":
            tries==input("Введите страну.")
        else:
            #здесь каждый проход пользователем засчитывается программой, и
            #вычитываем попытки до лимита 3
                print("Не то. Осталось попыток(до 3 попыток):", 3-d)    
                print("Вот подсказка: ",hint)
                tries=input("Введите страну: ")
                d+=1
    d+=0
    print("Ты угадал. Теперь ты можешь отправиться в эту страну.")
    return

def main():
    enigma=dictionary()
    game(enigma)
    

if __name__=="__main__":
    main()
    

    

        
        
