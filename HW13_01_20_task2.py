from random import randint
a = []
c = []
for i in range(10):
    a.append(randint(10, 1000))
print(a)
for i in range(9):
    b = []
    for j in range(len(a)):
        n = a[j]
        n //= 10
        if n >= 10:
            n //= 10
        if n == i+1:
            b.append(a[j])
    b.sort()
    for m in range(len(b)):
        c.append(b[m])
print(c)