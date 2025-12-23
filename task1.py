s = input().strip()

count = 0
for i in range(len(s) - 4):
    sub = s[i:i+5]
    if sub == ">>-->" or sub == "<--<<":
        count += 1

print(count)
