
def return_binary_or_hexa(num_tuple):
    a = num_tuple[15]
    b = num_tuple[57]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[16:57])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    elif sum_missing_nums % 2 == 0 and sum_missing_nums != 0:
        return hex(sum_missing_nums)[2:]
    else:
        return ""
