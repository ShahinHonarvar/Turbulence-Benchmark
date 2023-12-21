
def return_binary_or_hexa(num_tuple):
    a = num_tuple[56]
    b = num_tuple[90]
    sum_not_in_range = sum(set(range(a + 1, b)) - set(num_tuple[56:91]))
    if sum_not_in_range % 2 == 0:
        return hex(sum_not_in_range)[2:]
    else:
        return bin(sum_not_in_range)[2:]
