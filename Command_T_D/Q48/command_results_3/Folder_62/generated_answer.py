
def return_binary_or_hexa(test_tup):
    res = test_tup[50] + 1
    cnt = 0
    while cnt < len(test_tup) - 1:
        if test_tup[cnt] + 1 < test_tup[cnt + 1]:
            break
        else:
            cnt += 1
        res += test_tup[cnt] - test_tup[cnt - 1]
    if res % 2 == 1:
        return format(res, 'b')
    else:
        return format(res, 'x')
