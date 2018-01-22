import random

# у меня программа создаст еще отдельный текстовый файл в папке,
# где все будет красиво в столбик и вразброс ( ну, здесь тоже вразброс выдаст )

def pronoun():
    with open("pronoun.txt", encoding="utf-8") as f:
         text=f.read()
         word=text.split("\n")
         return random.choice(word)

def noun():
    with open("noun.txt", encoding="utf-8") as g:
         text1=g.read()
         word1=text1.split("\n")
         return random.choice(word1)

def verb():
    with open("verb.txt", encoding="utf-8") as j:
         text2=j.read()
         word2=text2.split("\n")
         return random.choice(word2)        

def determinativo():
    with open("determinativo.txt", encoding="utf-8") as p:
         text3=p.read()
         word3=text3.split("\n")
         return random.choice(word3)        

def inf():
    with open("inf.txt", encoding="utf-8") as r:
         text4=r.read()
         word4=text4.split("\n")
         return random.choice(word4)
        
def vopros():
    with open("vopros.txt", encoding="utf-8") as v:
         text5=v.read()
         word5=text5.split("\n")
         return random.choice(word5)
      
def adverb():
    with open("adverb.txt", encoding="utf-8") as s:
         text6=s.read()
         word6=text6.split("\n")
         return random.choice(word6)

def utverditel():
    sentence1 = pronoun() + " " + verb() + " " + determinativo() + " " + noun() + "."
    sentence1 = sentence1.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as q:
        q.write(sentence1 + '\n')

def voprositel():
    sentence2 = vopros() + " " + pronoun() + " " + verb() + " " + adverb()+ "?"
    sentence2 = sentence2.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as q:
        q.write(sentence2 + '\n')

def otrizatel():
    sentence3 = pronoun() + " " + "non" + " " + verb() + " " + determinativo()+ " " + noun() + "." 
    sentence3 = sentence3.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as q:
        q.write(sentence3 + '\n')


def uslovn():
    sentence4 = "se" + " " + verb() + " " + inf() + " " + "-" + " " + verb() + " " + inf() + "."
    sentence4 = sentence4.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as q:
        q.write(sentence4 + '\n')

def pobuditel():
    sentence5 = verb() + " " + adverb() + ","  + " " + "basta" + " " + verb() + "!"
    sentence5 = sentence5.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as q:
        q.write(sentence5 + '\n')

 
def masterpiece():
    uslovn()
    pobuditel()
    otrizatel()
    voprositel()
    utverditel()
    
    with open('text.txt',encoding='utf-8') as q:
        words = q.read()
        word = words.split('\n')
        random.choice(word)
        result = ''.join(word)
        print(result)
        
masterpiece()
    

      
