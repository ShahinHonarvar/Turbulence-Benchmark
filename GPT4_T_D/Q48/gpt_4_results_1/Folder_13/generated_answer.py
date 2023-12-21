
def return_binary_or_hexa(input_tuple):
    a = input_tuple[46]
    b = input_tuple[91]
    to_remove = set(input_tuple[47:91])
    total_set = set(range(a + 1, b))
    absent_set = total_set - to_remove
    sum_absent = sum(absent_set)
    if sum_absent % 2 == 0:
        return hex(sum_absent)[2:].upper()
    else:
        return bin(sum_absent)[2:]
