
def return_binary_or_hexa(int_tuple):
    
    a,b = int_tuple[15], int_tuple[57]
    missed_range_values = set(range(a + 1, b)) - set(int_tuple[15:58])
    sum_values = sum(missed_range_values)
    
    if sum_values == 0:
        return ''
    elif sum_values % 2 == 0:
        return hex(sum_values)[2:]
    else:
        return bin(sum_values)[2:]
