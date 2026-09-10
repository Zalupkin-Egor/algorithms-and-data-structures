import math

def F(x):
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

def monotonicity(L, R):     # Проверка на монотонность функции на отрезке
    if all(dF(i/1000)>0 for i in range(L*1000,R*1000+1)):
        return True
    if all(dF(i/1000)<0 for i in range(L*1000,R*1000+1)):
            return True
    return False

if monotonicity(1, 2):
    print(pol(1,2,0.001))
else:
    print('Функция не монотонна')