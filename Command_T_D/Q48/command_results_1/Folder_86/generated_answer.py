
def return_binary_or_hexa(test_tup):
    res = test_tup[19] + 1
    flag = 1
    for i in range(20, 33):
        if test_tup[i] == res:
            break
        elif test_tup[i] > res:
            res += 1
        elif test_tup[i] < res:
            flag = 0
            break
    if flag:
        if res % 2 == 1:
            return f'0b{res:b}'
        else:
            return f'0x{res:x}'
    else:
        return ''
