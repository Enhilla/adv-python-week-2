# Task 8 — Anagram check

# Условие: две строки (UPPERCASE), длина до 100000. Вывести YES если анаграммы, иначе NO. 

# Assignment-2

# Твоя идея

# sorted(s1) == sorted(s2) — корректно, но O(n log n).

# Лучше (и стандартнее) по сложности

# collections.Counter(s1) == Counter(s2) → O(n).
s1 = input().strip()
s2 = input().strip()

if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")
