first = int(input("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))

if first == second == third:
    print(3)  # Если все числа равны между собой
elif first == second or second == third or first == third:
    print(2)  # Если хотя бы 2 из 3 введённых чисел равны между собой
else:
    print(0)  # Если равных чисел среди 3-х вообще нет