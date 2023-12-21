
import itertools

def return_binary_or_hexa(test_tup):
    for idx in range(33, 78):
        if idx not in test_tup:
            break
    else:
        return ''
    num_sum = sum(test_tup)
    odd = num_sum % 2
    if odd:
        return bin(num_sum).zfill(8)
    else:
        return hex(num_sum).zfill(4)
