
def return_binary_or_hexa(tup):
    a, b = tup[22], tup[24]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(tup[22: 25]))
    
    if missing_nums_sum % 2 == 0:
        return format(missing_nums_sum, 'x')
    else:
        return format(missing_nums_sum, 'b')
