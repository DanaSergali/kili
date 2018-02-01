print("Aigy Paigy, поиграем")
letters=set("QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm")
#я взяла латинские согласные, а не русские, т.к. в примере английский
word=input("Введите слово или фразу, и прога переведет его на эйги-пэйги: ")
for letter in letters:
    word=word.replace(letter,letter+"aig")
#replace заменяет все вхождения одной строки на другую
print(word)    
