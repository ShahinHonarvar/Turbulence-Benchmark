
def return_binary_or_hexa(test_tup):
    res = test_tup[13] + 1
    x = test_tup[35] - 1
    if res <= x:
        if res % 2 == 0:
            return "0x{:x}".format(res)
        else:
            return "0b{:b}".format(res)
    else:
        return ""
