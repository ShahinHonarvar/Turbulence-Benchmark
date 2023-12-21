
def return_binary_or_hexa(test_tup):
    # sort the test_tup
    test_tup.sort()

    # set the first and last element of the range
    idx_a = test_tup.index(56)
    idx_b = test_tup.index(88)

    # set the range
    idx_a += 1
    idx_b -= 1

    # sum up the range
    sum_range = idx_b - idx_a

    # check if sum_range is odd
    if sum_range % 2 == 0:
        return hex(sum_range)
    else:
        return f'0b{sum_range:b}'
