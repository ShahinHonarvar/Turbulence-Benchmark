
def return_binary_or_hexa(test_tup):
    a, b = test_tup[1] - 1, test_tup[7] - 1
    x = sum(i for i in range(a + 1, b))
    if x % 2 == 0:
        return hex(x)[2:]
    else:
        return f'0b{bin(x)[2]:b}'
