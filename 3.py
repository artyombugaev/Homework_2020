from random import randint
N = 10
a = []
b = 10
c = 0
d = []
for i in range(N):
    a.append(randint(10, 1000))
print(a)

for i in range(N-1):
    for j in range(N-i-1):
        while b == 1001:
            if a[j] % b == 0:
                d.append(a[j])
            b *= 10
            if a[j] % b == 0:
                d.append(a[j])
            b /= 10
            b += 1
print(d)