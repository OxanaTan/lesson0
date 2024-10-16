def password(n):
    password = ""
    pairs_used = set()

    for i in range(1, 21):
        for j in range(i, 21):
            if i + j <= n * 2:
                pair_sum = i + j
                if n % pair_sum == 0:
                    pair = (i, j)
                    if pair not in pairs_used:
                        pairs_used.add(pair)
                        password += f"{i}{j}"

    return password


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    your_password = password(n)
    print(f"Пароль для числа {n}: {your_password}")
else:
    print("Число должно быть от 3 до 20.")
