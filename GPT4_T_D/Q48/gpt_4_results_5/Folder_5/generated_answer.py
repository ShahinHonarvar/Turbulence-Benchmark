
def return_binary_or_hexa(input_tuple):
    a = input_tuple[2]
    b = input_tuple[8]
    missing_numbers = set(range(a+1, b)) - set(input_tuple[2:9])
    sum_missing = sum(missing_numbers)
    
    if sum_missing == 0:
        return ''

    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
