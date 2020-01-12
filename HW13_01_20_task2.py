from random import randint
a = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []
b8 = []
b9 = []
c = []
for i in range(10):
    a.append(randint(10, 1000))
print(a)
for i in range(10):
    n = a[i]
    n //= 10
    if n >= 10:
        n //= 10
    if n == 1:
        b1.append(a[i])
    elif n == 2:
        b2.append(a[i])
    elif n == 3:
        b3.append(a[i])
    elif n == 4:
        b4.append(a[i])
    elif n == 5:
        b5.append(a[i])
    elif n == 6:
        b6.append(a[i])
    elif n == 7:
        b7.append(a[i])
    elif n == 8:
        b8.append(a[i])
    elif n == 9:
        b9.append(a[i])
b1.sort()
b2.sort()
b3.sort()
b4.sort()
b5.sort()
b6.sort()
b7.sort()
b8.sort()
b9.sort()
for i in range(len(b1)):
    c.append(b1[i])
for i in range(len(b2)):
    c.append(b2[i])
for i in range(len(b3)):
    c.append(b3[i])
for i in range(len(b4)):
    c.append(b4[i])
for i in range(len(b5)):
    c.append(b5[i])
for i in range(len(b6)):
    c.append(b6[i])
for i in range(len(b7)):
    c.append(b7[i])
for i in range(len(b8)):
    c.append(b8[i])
for i in range(len(b9)):
    c.append(b9[i])
print(c)