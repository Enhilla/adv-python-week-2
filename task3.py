# Task 3 — Equation for fifth-graders

s = input().strip()

a = s[0]      # первый символ
op = s[1]     # + или -
b = s[2]      # третий символ
c = s[4]      # правая часть

def val(ch):
    return None if ch == 'x' else int(ch)

A = val(a)
B = val(b)
C = val(c)

if op == '+':
    if A is None:
        x = C - B
    elif B is None:
        x = C - A
    else:
        x = A + B
else:
    if A is None:
        x = C + B
    elif B is None:
        x = A - C
    else:
        x = A - B

print(x)
