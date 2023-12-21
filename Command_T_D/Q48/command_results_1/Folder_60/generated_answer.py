
def return_binary_or_hexa(test_tup):
    a, b = test_tup[38], test_tup[52]
    return (b - a - 1) % 2 and "0b{:b}".format(a + 1 + (b - a - 1)) or "0x{:x}".format(a + 1 + (b - a - 1))
