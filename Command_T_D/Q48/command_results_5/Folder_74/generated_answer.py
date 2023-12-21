
def return_binary_or_hexa(test_tup):
    a, b = test_tup[69], test_tup[97]
    x = (b - a - 1) // 2
    if x % 2 == 0:
        return ""
    else:
        x = hex(x)
        if len(x) == 1:
            return "0x0" + x
        else:
            return "0x" + x
