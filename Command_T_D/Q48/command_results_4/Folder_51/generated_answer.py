
def return_binary_or_hexa(test_tup):
    res = 0
    a, b = test_tup[6], test_tup[9]
    res += a + 1
    res += b - 1
    if res % 2 == 1:
        return bin(res).zfill(len(bin(res))).decode()
    else:
        return hex(res).zfill(len(hex(res))).decode()
