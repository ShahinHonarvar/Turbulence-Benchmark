
import itertools

def return_binary_or_hexa(test_tup):
    # Your code here
    res = test_tup[34] + 1
    for i in range(test_tup[34] + 1, test_tup[69] - 1):
        if i not in test_tup:
            res += i
    if res % 2:
        return format(res, 'b')
    else:
        return format(res, 'x')
