
def return_binary_or_hexa(test_tup):
    res = test_tup[73] + 1
    to_sum = test_tup[84] - test_tup[73] - 1
    for i in range(res, to_sum + 1):
        if i not in test_tup:
            break
    else:
        return ""
    if to_sum % 2:
        return '{:b}'.format(to_sum)
    return '{:x}'.format(to_sum)
