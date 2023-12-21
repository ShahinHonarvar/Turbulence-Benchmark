
def return_binary_or_hexa(num_tuple):
    sum_missing = sum(set(range(num_tuple[30] + 1, num_tuple[200])) - set(num_tuple[30:201]))

    if sum_missing == 0:
        return ''

    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
