
def return_binary_or_hexa(tup):
    a, b = tup[56], tup[88]
    s = a + 1
    r = b - 1
    res = 0
    while s < r:
        if tup[s] == tup[r]:
            r -= 1
        else:
            res += 1
        s += 1
    if res % 2:
        return f'0b{res}'
    return f'0x{res:x}'
