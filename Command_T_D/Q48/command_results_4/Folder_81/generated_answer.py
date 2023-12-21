
def return_binary_or_hexa(test_tup):
    res = test_tup[10] + 1
    j = 10
    while j < test_tup[100]:
        if res not in test_tup[j:]:
            break
        res += 1
        j += 1
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
