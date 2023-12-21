
def return_binary_or_hexa(test_tup):
    a, b = test_tup[45], test_tup[48]
    x = (b - a - 1) // 2
    if x % 2 == 0:
        return ""
    elif x > 0:
        return ("{:b}".format(x), "0x{:x}".format(x))
    else:
        return ("{:b}".format(a + 1), "0x{:x}".format(a + 1))
