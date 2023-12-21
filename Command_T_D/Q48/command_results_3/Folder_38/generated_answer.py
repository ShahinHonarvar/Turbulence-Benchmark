
import re
def return_binary_or_hexa(lst):
    a, b = sorted(set(lst[36:85])), key=lambda x: x)
    if b - a > 2:
        return ''
    return str(sum(range(a + 1, b - 1)))[1:-1] if sum(range(a + 1, b - 1)) % 2 else hex(sum(range(a + 1, b - 1)))[1:-1]
