import math

# Задача 1

def F(x):   # Исходная функция
    return 0.1*(x**2) - x * math.log(x)

def pol(L,R,eps):       # Поиск корней методом половинного деления
    if F(L) * F(R)<0:
        while (R-L>eps):
            B = L+(R-L)/2
            if F(L)*F(B)<0:
                R = B
            else:
                L = B
        return((L+R)/2)
    else:
        return('Метод неприменим')

def dF(x):      # Производная функции
    return 0.2 * x - math.log(x) - 1

def monot(L, R):     # Проверка на монотонность функции на отрезке
    if all(dF(i/10000) > 0 for i in range(L*10000, R*10000+1)):
        return True

    if all(dF(i/10000) < 0 for i in range(L*10000, R*10000+1)):
        return True

    return False

if monot(1, 2):
    print(pol(1, 2, 0.0001))
else:
    print('Функция не монотонна')

# Задача 2

def F(x,A):
    return x*x-A

def sqrt_hord(x, eps):
    if x < 0:   # Проверка на отрицательное число
        return 'У отрицательных чисел нет корней'
    if x in (0,1):  
        return x
    a = 0 if x < 1 else 1   #
    b = max(x,1)

    fa = F(a, x)
    fb = F(b, x)

    k = 0
    xk = a
    xk1 = a + 2 * eps

    while abs(xk - xk1) > eps:  # Итерации продолжаются, пока разность между шагами превышает погрешность
        k += 1
        xk1 = xk
        xk = a - (fa * (b-a)) / (fb - fa)
        fx = F(xk,x)
        if fx == 0:
            return xk
        if fx * fb > 0:
            b = xk
            fb = fx
        else:
            a = xk
            fa = fx
    return xk

print(sqrt_hord(16, 0.0001))