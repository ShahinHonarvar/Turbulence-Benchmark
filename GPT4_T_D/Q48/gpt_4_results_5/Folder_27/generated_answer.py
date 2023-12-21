
def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    
    missing_values_sum = sum(set(range(a + 1, b)) - set(tup[86: 90]))
    
    if missing_values_sum == 0:
        return ""
    elif missing_values_sum % 2 == 0:   
        return format(missing_values_sum, 'x')
    else:
        return format(missing_values_sum, 'b')
