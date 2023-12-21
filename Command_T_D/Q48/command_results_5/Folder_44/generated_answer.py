
def return_binary_or_hexa(test_tup):
    res = test_tup[36] + 1
    while res < test_tup[52]:
        if res in test_tup:
            break
        res += 1
    if res in test_tup:
        return ''
    if res % 2 == 0:
        return hex(res)[2:-1]
    return '0b' + bin(res)[2:]
