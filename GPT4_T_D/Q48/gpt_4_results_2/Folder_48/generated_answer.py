
def return_binary_or_hexa(num_tuple):
    a = num_tuple[933]
    b = num_tuple[996]
    sum_missing = sum(set(range(a + 1, b)) - set(num_tuple[933:997]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
