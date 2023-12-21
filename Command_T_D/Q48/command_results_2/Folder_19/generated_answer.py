
def return_binary_or_hexa(test_tup):
    res = test_tup[1] + 1
    while res <= test_tup[4]:
        if res not in test_tup:
            break
        res += 1
    if res == test_tup[4]:
        return ""
    if res % 2 == 0:
        return hex(res)[2:]
    return bin(res)[2:]
