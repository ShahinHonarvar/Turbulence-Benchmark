
def return_binary_or_hexa(num_tuple):
    a = num_tuple[3]
    b = num_tuple[8]
    set_nums = set(num_tuple[4:8])

    sum_values = sum(set(range(a+1, b)) - set_nums)

    if sum_values == 0:
        return ""
    elif sum_values % 2 == 1:
        return bin(sum_values)[2:]
    else:
        return hex(sum_values)[2:].upper()
