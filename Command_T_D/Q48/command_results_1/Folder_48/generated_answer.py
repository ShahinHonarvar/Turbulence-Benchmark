
def return_binary_or_hexa(test_tup):
    res = test_tup[933] + 1
    for i in range(934, 996):
        if test_tup[i] == res:
            break
        res += 1
    if res % 2 == 1:
        return f'0b{res}'
    else:
        return f'0x{res}'
