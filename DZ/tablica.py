a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите ответ: '))
if a * b == c:
    print('Ваш ответ правильный: ')
    print(a * b)
elif a * b < c or a * b > c:
    print('Неверно! Правильный ответ: ', a * b,)
