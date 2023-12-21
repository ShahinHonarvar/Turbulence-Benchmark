
def return_binary_or_hexa(tuple):
    a = tuple[3]
    b = tuple[9]
    numbers_between = set(range(a+1, b))
    numbers_in_tuple = set(tuple[3:10])
    missing_numbers = numbers_between - numbers_in_tuple
    sum_missing = sum(missing_numbers)
    
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
