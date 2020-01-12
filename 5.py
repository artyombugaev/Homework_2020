a = int(input('Введите число: '))
if a == 0:
    print('Ошибка - число = 0')
    exit(0)
elif a > 0:
    if a > 100:
        print('Ошибка - в числе больше 3 знаков')
        exit(0)
    print('Положительное')
    if a < 10:
        print('Однозначное')
    elif a >= 10:
        print('Двузначное')
    if a % 2 == 0:
        print('Чётное')
    elif a % 2 == 1:
        print('Нечётное')
elif a < 0:
    if a < -100:
        print('Ошибка - в числе больше 3 знаков')
        exit(0)
    print('Отрицательное')
    if a > -10:
        print('Однозначное')
    elif a <= -10:
        print('Двузначное')
    if a % 2 == 0:
        print('Чётное')
    elif a % 2 == 1:
        print('Нечётное')