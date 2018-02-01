print("Pig Latin это языковая игра..")

letters=set("ЁУЕЫАОЭЯИЮёуеыаоэяию")
word=input("Введите слово или фразу, и прога переведет его на PIG LATIN: ")
for letter in letters:
    word=word.replace(letter,letter+"c"+letter)
#replace заменяет все вхождения одной строки на другую
print(word)    
