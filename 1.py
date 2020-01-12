from random import randint
a = []
c = []
b = 0
for i in range(15):
    a.append(randint(-50, 50))
print(a)
a.sort()
a.reverse()
print(a)
for i in range(15):
    if a[i] > 0 & a[i] % 2 == 0:
        c.append(a[i])
print(c)
