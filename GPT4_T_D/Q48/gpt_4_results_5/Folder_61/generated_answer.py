
def return_binary_or_hexa(num_tuple):
    a = num_tuple[0]
    b = num_tuple[8]

    not_in_tuple = list(set(range(a+1, b)) - set(num_tuple[0:9]))
    sum_not_in_tuple = sum(not_in_tuple)

    if not not_in_tuple:
        return ""
    elif sum_not_in_tuple % 2 != 0:
        return format(sum_not_in_tuple, 'b')
    else:
        return format(sum_not_in_tuple, 'x')
