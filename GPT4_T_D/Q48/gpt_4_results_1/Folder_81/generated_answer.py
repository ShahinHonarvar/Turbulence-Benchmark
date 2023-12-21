
def return_binary_or_hexa(number_tuple):
    a = number_tuple[10]
    b = number_tuple[100]
    missing_numbers = set(range(a+1, b)) - set(number_tuple[10:101])
    missing_sum = sum(missing_numbers)

    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return format(missing_sum, 'b') 
    else:
        return format(missing_sum, 'X')
