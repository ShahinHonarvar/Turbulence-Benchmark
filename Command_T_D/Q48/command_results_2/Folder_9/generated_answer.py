
def return_binary_or_hexa(test_tup):
    a, b = test_tup[70], test_tup[200]
    if b - a > 1:
        return (b - a - 1) % 2 + "0b" + bin(a + 1)[2:]
    return (a + 1) % 2 + "0b" + bin(b - 1)[2:]
