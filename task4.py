# Условие: дано n, m (1 ≤ m ≤ n ≤ 100) и строка длины n. Сколько различных подстрок длины m есть в строке. 

# Assignment-2

# Идея

# Все подстроки длины m добавить в set, в конце вывести len(set).

# Структура

# ввод n, m

# ввод строки s

# subs = set()

# цикл по i: 0..n-m

# subs.add(s[i:i+m])

# вывести len(subs)
n, m = map(int, input().split())
s = input().strip()

subs = set()
for i in range(n - m + 1):
    subs.add(s[i:i + m])

print(len(subs))
