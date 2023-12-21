
def return_binary_or_hexa(tuple_int):
    a = tuple_int[2]
    b = tuple_int[5]
    sum_value = sum(set(range(a + 1, b)) - set(tuple_int[2:6]))
    if sum_value == 0:
        return ""
    elif sum_value % 2 == 0:
        return hex(sum_value)[2:].upper()
    else:
        return bin(sum_value)[2:]
