
def return_binary_or_hexa(test_tup):
    test_tup = list(test_tup)
    a = test_tup[42]
    b = test_tup[87]
    x = (b - a) // 2
    y = b - a - x
    if x > 0 and y > 0:
        res = str(a + x + y)
        if len(res) % 2 == 0:
            return res
        else:
            return '0b' + res
    else:
        res = hex(a + x + y)
        return res
