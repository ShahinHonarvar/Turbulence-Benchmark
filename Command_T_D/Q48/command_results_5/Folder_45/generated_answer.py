
def return_binary_or_hexa(test_tup):
    # sort the test_tup in ascending order
    test_tup.sort()
    # define a and b
    a = test_tup[30]
    b = test_tup[200]
    # define the sum
    sum_ = b - a - 1
    # check if the sum is odd
    if sum_ % 2 == 1:
        # return the binary representation of the sum
        return '{:b}'.format(sum_)
    else:
        # return the hexadecimal representation of the sum
        return '{:x}'.format(sum_)
