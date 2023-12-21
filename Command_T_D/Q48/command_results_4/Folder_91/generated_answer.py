
def return_binary_or_hexa(test_tup):
    res = test_tup[0] + 1
    idx = 1
    while idx < 7:
        if test_tup[idx] == test_tup[idx - 1]:
            break
        elif test_tup[idx] == res:
            res += 1
        else:
            return str(test_tup[idx] + 1)
        idx += 1
    return str(test_tup[0] + 1)
