# Условие: дана строка (≤250 символов). Посчитать количество подстрок, равных >>--> или <--<<.  # pyright: ignore[reportUndefinedVariable]

# Assignment-2

# Идея

# Пройти по всем позициям i, взять подстроку длины 5: s[i:i+5], сравнить с двумя шаблонами. # type: ignore

# Структура

# ввод строки s

# цикл for i in range(len(s)-4) (чтобы i+5 не вышло за границы)

# срез sub = s[i:i+5]

# проверка, счётчик
s = input().strip()

count = 0
for i in range(len(s) - 4):
    sub = s[i:i+5]
    # len(s)-4 потому что нам нужны окна длины 5: i..i+4
    if sub == ">>-->" or sub == "<--<<":
        count += 1

print(count)
