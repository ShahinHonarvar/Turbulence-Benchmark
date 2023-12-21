
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[42], test_tup[87]
    if a + 1 <= b - 1:
        res = str(sum(range(a + 1, b - 1)))
    if res:
        if len(res) % 2 == 1:
            res = '0b' + res
        else:
            res = '0x' + res
    return res
