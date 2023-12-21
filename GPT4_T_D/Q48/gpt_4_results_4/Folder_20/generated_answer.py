
def return_binary_or_hexa(t):
    
    a = t[27]
    b = t[96]
    
    sum_result = sum(set(range(a + 1, b)) - set(t[27:97]))

    if sum_result % 2 == 0:
        return format(sum_result, 'x')
        
    else:
        return format(sum_result, 'b')
