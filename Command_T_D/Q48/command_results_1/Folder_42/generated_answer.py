
def return_binary_or_hexa(test_tup):
    a, b = test_tup[18], test_tup[60]
    num = sum(x for x in range(a + 1, b))
    if num % 2 == 0:
        return hex(num)[2:]
    else:
        return bin(num)[2:]
