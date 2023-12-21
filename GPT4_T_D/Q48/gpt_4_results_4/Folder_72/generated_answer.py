
def return_binary_or_hexa(num_tuple):
    a = num_tuple[13]
    b = num_tuple[70]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[14:70])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
