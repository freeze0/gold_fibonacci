import math
#
# def f(x):
#     return x**2-4*x+5
#
# a = -4
# b = 6
# eps = 0.5
# l = 2 * eps
# k = 0
# betta = (3-math.sqrt(5)) / 2
# delta = abs(a-b)
# y = a + betta * (b - a)
# z = a + b - y
# while delta > l:
#     if f(y) <= f(z):
#         b = z
#         z = y
#         y = a + b - y
#     else:
#         a = y
#         y = z
#         z = a + b - z
#     delta = abs(a - b)
#     k+=1
#
#print('x* = ', (a + b)/2, '\n', 'принадлежит отрезку', a, b, '\n', 'c погрешностью =', round((b - a)/2, 2), '\n', 'за к шагов = ', k)

import math


# Вычисление числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Определение минимального значения функции в заданном диапазоне с использованием метода Фибоначчи
def fibonacci_search(func, a, b, n, eps):
    # Инициализация переменных
    l = 2*eps
    delta = 0.2
    k = 1
    z = a + ((fibonacci(n - k - 1) / fibonacci(n - k + 1)) * (b - a))
    y = a + b - z
    fz = func(z)
    fy = func(y)
    # Пока не достигнута заданная точность
    while k <= n - 3:
        print('Сравниваем f(yk) с f(zk)')
        print(f'f(y{k}) = {fy}, f(z{k}) = {fz} =>')
        if fz < fy:
            print(f'f(y{k}) <= f(z{k})')
            print(
                f'Таким образом, a{k + 1} = a{k} = {a}; b{k + 1} = z{k} = {z}; '
                f'y{k + 1} = a{k + 1} + b{k + 1} - y{k} = {a + b - y}; z{k + 1} = y{k} = {y}')
            b = y
            y = z
            fy = fz
            z = a + ((fibonacci(n - k - 1) / fibonacci(n - k + 1)) * (b - a))
            fz = func(z)
        else:
            print('f(y{k}) > f(z{k})')
            print(
                f'Таким образом, a{k + 1} = y{k} = {y}; b{k + 1} = b{k} = {b}; '
                f'y{k + 1} = z{k} = {z}; z{k + 1} = a{k + 1} + b{k + 1} - z{k} = {a + b - y}')
            a = z
            z = y
            fz = fy
            y = a + ((fibonacci(n - k) / fibonacci(n - k + 1)) * (b - a))
            fy = func(y)
        k += 1

    # Возвращаем значение, близкое к минимуму
    return (a + b) / 2


# Пример использования
func = lambda x: x**2-4*x+5
a = -4
b = 6
n = 19
eps = 0.5
result = fibonacci_search(func, a, b, n, eps)

# Вывод результата
print("Минимальное значение функции: ", result)
