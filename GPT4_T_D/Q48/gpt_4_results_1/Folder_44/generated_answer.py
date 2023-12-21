
def return_binary_or_hexa(num_tuple):
    a = num_tuple[36]
    b = num_tuple[52]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(num_tuple[37:53]))
    if missing_nums_sum == 0:
        return ""
    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:]
    else:
        return bin(missing_nums_sum)[2:]
