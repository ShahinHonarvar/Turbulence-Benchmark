
import itertools

def return_binary_or_hexa(s):
    a, b = s[86], s[90]
    s = set(s)
    if b - a > 1:
        x = sum(i for i in range(a + 1, b - 1) if i not in s)
        return hex(x)[2:] if x % 2 == 0 else f'{x:b}'
