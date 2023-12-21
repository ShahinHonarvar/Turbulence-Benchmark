
def return_binary_or_hexa(test_list):
    res = 0
    cnt = 0
    for i in range(20, 35):
        if test_list[i] not in test_list:
            res += test_list[i]
            cnt += 1
    if cnt % 2 == 1:
        return format(res, 'b')
    else:
        return format(res, 'x')
