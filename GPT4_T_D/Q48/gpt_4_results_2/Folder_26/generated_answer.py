
def return_binary_or_hexa(num_tuple):
    a = num_tuple[68]
    b = num_tuple[99]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(num_tuple[68:100]))
    if missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:]
    else:
        return bin(missing_nums_sum)[2:]
