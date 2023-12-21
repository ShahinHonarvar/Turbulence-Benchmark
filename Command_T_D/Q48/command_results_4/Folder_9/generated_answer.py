
def return_binary_or_hexa(test_tup):
    a, b = test_tup[70], test_tup[200]
    return ("0b" + bin(sum(x for x in range(a + 1, b - 1) if x not in test_tup[70:200])).zfill(8),
