
def return_binary_or_hexa(tuple_arg):
    a, b = tuple_arg[0], tuple_arg[5]
    missing_ints = set(range(a + 1, b)).difference(set(tuple_arg[:6]))
    sum_missing_ints = sum(missing_ints)
    if sum_missing_ints == 0:
        return ""
    elif sum_missing_ints % 2 == 0:
        return hex(sum_missing_ints)[2:]
    else:
        return bin(sum_missing_ints)[2:]
