
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[0], test_tup[6]
    c = a + 1
    x = a
    while c <= b - 1:
        if c in test_tup:
            break
        x += 1
        c += 1
    res = str(x)
    if len(res) == 1:
        res = '0' + res
    if res[0] == '0':
        res = '0b' + res
    else:
        res = '0x' + res
    return res
