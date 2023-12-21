
def return_binary_or_hexa(tup):
    a = tup[37]
    b = tup[43]
    missing_numbers_sum = sum(set(range(a+1, b)) - set(tup[38:43]))
    if missing_numbers_sum % 2 == 0:
        return format(missing_numbers_sum, 'x')
    else:
        return format(missing_numbers_sum, 'b')
