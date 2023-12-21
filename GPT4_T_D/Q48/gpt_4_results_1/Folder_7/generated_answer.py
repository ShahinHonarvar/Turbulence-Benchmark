
def return_binary_or_hexa(my_tuple):
    a = my_tuple[10]
    b = my_tuple[97]
    missing_nums = set(range(a + 1, b)) - set(my_tuple[10:97])
    sum_missing = sum(missing_nums)
    
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return ''
