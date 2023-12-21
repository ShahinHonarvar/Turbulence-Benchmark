
def return_binary_or_hexa(test_tup):
    a, b = test_tup[90], test_tup[200]
    s = sum(x for x in range(a + 1, b - 1))
    return "0b" + bin(s)[2:-1] if s % 2 else hex(s)[2:]
