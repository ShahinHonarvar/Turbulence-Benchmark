
def return_binary_or_hexa(input_tuple):
    a, b = input_tuple[17], input_tuple[88]
    sum_not_in_tuple = sum(set(range(a+1, b)) - set(input_tuple[17:89]))
    if sum_not_in_tuple == 0:
        return ''
    elif sum_not_in_tuple % 2 == 0:
        return hex(sum_not_in_tuple)[2:].upper()
    else:
        return bin(sum_not_in_tuple)[2:]
