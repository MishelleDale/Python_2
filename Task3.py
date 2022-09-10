# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
step = 1
sum = 0

while step < n+1:
    sum = sum + (1 + 1/step)**step
    step += 1
print(round(sum, 2))

