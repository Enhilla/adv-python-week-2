# Условие: номер длины 6: L D D D L L, где L ∈ {A,B,C,E,H,K,M,O,P,T,X,Y}, цифры любые 0–9. Вывести Yes/No для каждой строки. 

# Assignment-2

# Идея

# Проверить:

# длина = 6

# s[0], s[4], s[5] в allowed

# s[1:4] — все цифры

# Структура

# создать allowed

# прочитать n

# цикл n раз:

# прочитать s

# флаг ok

# проверки

# print


allowed = set("ABCEHKMOPTX Y".replace(" ", ""))  # ABCEHKMOPTXY

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    ok = True

    if len(s) != 6:
        ok = False
    else:
        if s[0] not in allowed:
            ok = False
        # три цифры подряд
        if not (s[1].isdigit() and s[2].isdigit() and s[3].isdigit()):
            ok = False
        if s[4] not in allowed or s[5] not in allowed:
            ok = False

    print("Yes" if ok else "No")
