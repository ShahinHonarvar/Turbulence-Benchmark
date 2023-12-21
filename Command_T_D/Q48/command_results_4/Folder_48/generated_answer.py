
def return_binary_or_hexa(test_tup):
    # sort input test_tup
    test_tup = sorted(test_tup)
    # calculate sum of integers from a + 1 to b - 1
    last = test_tup[933] + 1
    curr = test_tup[933] + 1
    res = 0
    while curr <= test_tup[996]:
        if curr not in test_tup:
            res += curr
        curr += 1
    # convert sum to binary or hexadecimal representation
    if res % 2 == 1:
        return f'{res:b}'
    else:
        return f'{res:x}'
