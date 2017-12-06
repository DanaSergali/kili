with open("text.txt", "w", encoding="utf-8") as f:
    number = []
    for i in range(7):
        number.append(input("Введите, пожалуйста, число: "))
    for i in range(7):
        for m in range(int(number[i])):
            f.write("X")
        f.write("\n")
with open("text.txt", encoding="utf-8") as f:
    text = f.read()
    print(text)
