
import operator as o

def return_binary_or_hexa(test_list):
    res = sum(
        x
        for x in range(test_list[55] + 1, test_list[84] - 1)
        if x not in test_list[55:84]
    )
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
