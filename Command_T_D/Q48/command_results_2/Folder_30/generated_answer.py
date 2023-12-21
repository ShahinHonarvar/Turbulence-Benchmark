
def return_binary_or_hexa(test_tup):
    res = test_tup[22] + 1
    while res < test_tup[24]:
        if test_tup[22] <= res <= test_tup[24]:
            continue
        res += 1
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
