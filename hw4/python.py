 # Variant №6
with open("text.txt") as f:
    text = f.read().split(' ')
    m = 0
    for d in text:
       if d.istitle():
            m = m + 1
    print("процент слов, которые начинаются с большой буквы: %.2f %%" %(m/len(text)*100))
