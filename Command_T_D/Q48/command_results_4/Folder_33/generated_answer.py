
def return_binary_or_hexa(test_tup):
    res = 0
    s = ""
    a = test_tup[13]
    b = test_tup[35]
    for x in range(a + 1, b - 1):
        if x not in test_tup:
            res += x
            if res % 2 == 1:
                s += '1'
            else:
                s += '0'
    if s:
        if len(s) == 1:
            return '0b' + s
        return '0b' + s[::-1]
    else:
        return '0x' + hex(res)[2:]
