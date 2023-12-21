
def return_binary_or_hexa(nbr_tuple):
    a = nbr_tuple[32]
    b = nbr_tuple[44]
    sum_val = 0
    present_numbers = set(nbr_tuple[32:45])
    for i in range(a + 1, b):
        if i not in present_numbers:
            sum_val += i
    if sum_val == 0:
        return ''
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
