
def return_binary_or_hexa(test_tup):
    # insert your code here
    a, b = test_tup[46], test_tup[91]
    res = sum(x for x in range(a + 1, b - 1) if x not in test_tup[46:91])
    if res % 2:
        return bin(res).zfill(len(bin(res)) - 2)
    else:
        return hex(res)[2:-1]
