
def return_binary_or_hexa(tuple_):
    a = tuple_[20]
    b = tuple_[51]
    tuple_section = tuple_[21:51]
    sum_in_range = sum(set(range(a + 1, b)) - set(tuple_section))
    if sum_in_range == 0:
        return ''
    elif sum_in_range % 2 == 0:
        return hex(sum_in_range)[2:].upper()
    else:
        return bin(sum_in_range)[2:]    
