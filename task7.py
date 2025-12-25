# Task 7 — Shopping List Analysis

# # Условие: по списку покупок в одной строке:

# частоты

# самый частый

# купленные ровно 1 раз

# отсортировать по убыванию частоты 



# Идея

# Словарь freq, затем:

# печать частот

# max(freq, key=freq.get)

# фильтр count==1

# sorted(freq.items(), key=lambda x: -x[1])

# Важно про формат

# В примере после Purchase frequency: идут строки item: count, потом без пустой строки “Most popular item: ...”, потом “Purchased once: ...” (у тебя есть лишние \n, но обычно это не критично; иногда автотесты требуют точный формат).
items = input().split()

freq = {}


for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Purchase frequency:")
for item in freq:
    print(f"{item}: {freq[item]}")

most_popular = max(freq, key=freq.get)
print("\nMost popular item:", most_popular)

print("\nPurchased once:", end=" ")
for item in freq:
    if freq[item] == 1:
        print(item, end=" ")

print("\n\nSorted by frequency:")

sorted_items = sorted(freq.items(), key=lambda x: -x[1])
for item, count in sorted_items:
    print(item, count)
