
def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[51]
    b = nums_tuple[76]
    
    missing_nums_sum = sum(set(range(a + 1, b)) - set(nums_tuple[51:77]))
    
    if missing_nums_sum == 0:
        return ""
    elif missing_nums_sum % 2 == 0:
        return format(missing_nums_sum, 'x')
    else:
        return format(missing_nums_sum, 'b')
