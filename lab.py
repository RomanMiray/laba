import math

g = 9.8
e = 2.71

def task_1():
    print("===== Задание 1 =====")
    while True:
        try:
            n = int(input("Введите натуральное число: "))
        except ValueError:
            print("Ошибка! Нужно ввести натуральное число!")

        if n > 0:
            break
        else:
            print("Ошибка! Нужно ввести натуральное число!")

    total = 0.0
    start = 1
    end = n
    for i in range(start, end + 1):
        total += (1 + (1 / i ** 2))

    print("Ответ:  ", total)
    input("Нажмите любую клавишу чтобы вернуться в главное меню")

def task_2():
    print("===== Задание 2 =====")

    M = 80.0
    m1 = 400.0

    print(f"Переменные: {M}, {m1}.")

    for m2 in range(100, 301, 20):
        denominator = (m1 + m2 + (M/2)) 
        if denominator == 0:
            print(f"Ошибка! Знаменатель равен нулю!, m2 = {m2}")
            continue
        a = (m2 - m1)/denominator * g
        print(f"Значение 'a' равно {a}")

    input("Нажмите любую клавишу чтобы вернуться в главное меню")

def task_3():
    print("===== Задание 3 =====")

    p = 8.0
    Q0 = 2.0
    target_Q = 0.15

    lam = math.log(2) / p

    t = 0
    while True:
        Q = Q0 * (e ** (-lam * t))

        if Q <= target_Q:
            print(f"Мощность уменьшится до {target_Q} R/h через {t} days.")
            break

        t += 5

    input("Нажмите любую клавишу чтобы вернуться в главное меню")
    

def main():
    while True:
        print("\n=============")
        print("Главное меню")
        print("1. Выполнить первое задание")
        print("2. Выполнить второе задание")
        print("3. Выполнить третье задание")
        print("4. Выход")
        
        choice = input("Выберите опцию (1-4): ")
        
        if choice == '1':
            task_1()
        elif choice == '2':
            task_2()
        elif choice == '3':
            task_3()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Введите число от 1 до 4.")

if __name__ == "__main__":
    main()