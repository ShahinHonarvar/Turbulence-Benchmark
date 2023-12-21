
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(1, 7):
        res += test_tup[i]
    for j in range(1, res // 2 + 1):
        if res % 2 == 1:
            return f'0b{res - j}0'
        else:
            return f'0x{res - j:x}'
