
def return_binary_or_hexa(int_tuple):
    a, b = int_tuple[2], int_tuple[7]
    sum_absent = sum(set(range(a + 1, b)) - set(int_tuple[2:8]))
    if sum_absent % 2 != 0:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:] if sum_absent != 0 else ''
