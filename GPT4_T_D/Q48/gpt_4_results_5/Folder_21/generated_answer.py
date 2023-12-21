
def return_binary_or_hexa(num_tuple):
    a = num_tuple[15]
    b = num_tuple[57]
    tuple_range = num_tuple[16:57]
    absence_sum = sum(set(range(a + 1, b)) - set(tuple_range))

    if absence_sum == 0:
        return ''
    elif absence_sum % 2 == 1:
        return bin(absence_sum)[2:]
    else:
        return hex(absence_sum)[2:].upper()
