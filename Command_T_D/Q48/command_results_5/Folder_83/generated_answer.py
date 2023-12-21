
def return_binary_or_hexa(test_tup):
    if test_tup[90] == test_tup[200]:
        return ""
    x = test_tup[90] + 1
    y = test_tup[200] - 1
    cnt = 0
    for el in range(x, y):
        if el not in test_tup[90:200]:
            cnt += 1
    if cnt % 2 == 0:
        return hex(cnt)
    else:
        return bin(cnt)
