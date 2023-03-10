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

def f(x):
    return x**2-4*x+5

N = 19
fib = [1] * 2
for i in range(2, N):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib)
a = -4
b = 6
eps = 0.5
l = 2 * eps
k = 0
y = a + fib[N -]
z =
while k != N - 3:
