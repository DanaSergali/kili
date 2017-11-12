request = str(input('Write a word: '))
m = -1
print(request)
for d in request:
    result = request[:m]
    print(result)
    m -= 1
