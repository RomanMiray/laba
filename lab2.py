import math

g = 9.8
e = 2.71

def task_1():
    print("===== Task 1 =====")
    while True:
        try:
            n = int(input("Введите натуральное число: "))
        except ValueError:
            print("Введите числовое значение!")
            continue

        if n > 0:
            break
        else:
            print("Натуральное число!")

    total = 0.0
    start = 1
    end = n
    for i in range(start, end + 1):
        total += (1 + (1 / (i**2)))

    print(f"Значение равно {total}")
    input("Нажмите любую клавишу чтобы вернуться в главное меню!")

def task_2():
    print("===== Task 2 =====")

    M = 80.0
    m1 = 400.0

    print(f"Переменные: {M}, {m1}")

    for m2 in range(100, 301, 20):
        denominator = m1 + m2 + M/2
        if denominator == 0:
            print("Ошибка, знаменатель равен нулю!!")
            continue
        a = (m2 - m1)/denominator * g
        print(f"Значение переменной a = {a}")
        input("Нажмите любую клавишу чтобы вернуться в главное меню!")
        
def task_3():
    print("===== Task 3 =====")

    Q0 = 2.0
    p = 8
    target_Q = 0.15

    lam = math.log(2)/p

    t = 0
    while True:
        Q = Q0 * (e ** (-lam * t))

        if Q <= target_Q:
            print("Значение станет 0.15 через {t} дней")
            break

        t += 5

    input("Нажмите любую клавишу чтобы вернуться в главное меню!")


