print("Pig Latin это игра слов, поиграем? ")
phrase=input("Введите фразу или слово на английском(на латинице): ")
word=phrase.split(" ")
PigLatin=""
vowels=set("EYUIOAeyuioa")
for m in word:
    number_of_vowels=0
    for letter in m:
        if letter in vowels:
            pigw=m[number_of_vowels:]+ m[:number_of_vowels]+"ay"
            break
        number_of_vowels+=1
PigLatin=PigLatin+ " " +pigw
print(PigLatin)
