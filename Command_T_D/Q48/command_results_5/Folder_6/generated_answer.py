
import itertools

def return_binary_or_hexa(test_tup):
    # get the a and b indices
    a, b = sorted(test_tup)[20], sorted(test_tup)[93]
    # get the range of indices
    idx_range = range(a + 1, b)
    # get the range of values
    idx_values = list(map(str, idx_range))
    # use set to get the unique values
    idx_uniq = set(idx_values)
    # get the indices of unique values
    idx_uniq_idx = [i for i, v in enumerate(idx_values) if v in idx_uniq]
    # sum the indices
    idx_sum = sum(range(len(idx_uniq_idx)))
    # if the sum is odd return binary
    if idx_sum % 2 == 1:
        return format(idx_sum, 'b')
    # else return hexadecimal
    return format(idx_sum, 'x')
