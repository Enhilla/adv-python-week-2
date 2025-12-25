# Task 6 — all_eq(list) (у тебя решения НЕТ)

# Условие: написать функцию all_eq(list) которая выравнивает строки до длины самой длинной, дополняя справа _. Порядок не менять. 

# Assignment-2

# Правильная структура

# найти max_len = max(len(x) for x in lst)

# вернуть новый список: x + "_"*(max_len-len(x))

# Пример решения
def all_eq(lst):
    max_len = 0

    # находим максимальную длину
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    # дополняем строки
    result = []
    for s in lst:
        result.append(s + "_" * (max_len - len(s)))

    return result
print(all_eq(["hi", "hello", "hey"]))
# ['hi___', 'hello', 'hey__']
