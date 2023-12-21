
def return_binary_or_hexa(test_tup):
    a, b = test_tup[10], test_tup[12]
    if b - a - 1 <= 0:
        return ""
    test_tup_str = ", ".join(str(x) for x in test_tup)
    if a % 2 == b % 2:
        return "0x{:x}".format(a + 1 + (b - a - 1))
    else:
        return "0b{:b}".format(a + 1 + (b - a - 1))
