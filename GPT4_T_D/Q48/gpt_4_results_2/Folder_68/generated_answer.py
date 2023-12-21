
def return_binary_or_hexa(tuple_int):
    a = tuple_int[0]
    b = tuple_int[9]
    missing_int_sum = sum(set(range(a+1, b)) - set(tuple_int[1:9]))
    if missing_int_sum == 0:
        return ''
    elif missing_int_sum % 2 != 0:
        return bin(missing_int_sum)[2:]
    else:
        return hex(missing_int_sum)[2:]
