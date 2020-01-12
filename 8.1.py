c = []
s = 0
for i in range(6):
    c.append(int(input('Введите число: ')))
for e in c:
    if int(e) % 2 == 0:
        s += e
print(s)