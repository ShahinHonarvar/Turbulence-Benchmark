
def return_binary_or_hexa(test_tup):
    res = ""
    x = test_tup[50] + 1
    y = test_tup[200] - 1
    for i in range(x, y):
        if i not in test_tup:
            res += i
    if len(res) % 2 == 1:
        res = '0b' + res
    else:
        res = '0x' + res
    return res
