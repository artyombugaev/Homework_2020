a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))
d = int(input('Введите 4 число: '))
e = int(input('Введите 5 число: '))
f = int(input('Введите 6 число: '))
x = [a, b, c, d, e, f]
for y in x:
    if y % 2 == 0:
        print(y)