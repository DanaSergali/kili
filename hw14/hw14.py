import re
def readfile():
    with open("kenner.txt",encoding="utf-8") as f:
        text=f.read()
    return text

def cleartext(text):
    pattern=re.compile(r"[!|?|…|.]")
    clean=[re.sub(r"[^\s\d\w]","",d) for d in pattern.split(text)]
    return clean

def countfile(clean):
    i=0
    for d in range(0,len(clean)):
        clean[d]=[d for d in clean[d].split()]
        if len(clean[d])>=10:
            for word in clean[d]:
                i+=len(word)
            go=i/len(clean[d])
            print(" ".join(clean[d]))
            show(go)
        i=0

def show(go):
    print("Это предложение со словами длины... {:.1f}".format(go))

def main():
    countfile(cleartext(readfile()))

main()
