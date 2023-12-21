
def return_binary_or_hexa(test_tup):
    res = test_tup[86] + 1
    cnt = 0
    while cnt < len(test_tup) - 1:
        res += test_tup[cnt]
        cnt += 1
    if res % 2 == 0:
        return hex(res)
    else:
        return '0b' + bin(res)[2:-1]
