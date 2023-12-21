
def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    
    missing_numbers = set(range(a+1, b)) - set(t[34:70])
 
    total = sum(missing_numbers)

    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
