
def return_binary_or_hexa(int_tuple):
    a = int_tuple[10]
    b = int_tuple[100]
    set_diff = set(range(a + 1, b)) - set(int_tuple[10:101])
    sum_diff = sum(set_diff)
    if sum_diff == 0:
        return ""
    elif sum_diff % 2 == 1:
        return bin(sum_diff)[2:]
    else:
        return hex(sum_diff)[2:]
