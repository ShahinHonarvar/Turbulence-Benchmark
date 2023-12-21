
def return_binary_or_hexa(test_tup):
    a, b = test_tup[62], test_tup[96]
    res = sum(test_tup[a + 1:b])
    if res % 2 == 1:
        return bin(res).zfill(16)
    else:
        return hex(res).zfill(8)
