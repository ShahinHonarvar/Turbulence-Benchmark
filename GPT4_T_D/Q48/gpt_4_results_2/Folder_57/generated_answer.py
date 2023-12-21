
def return_binary_or_hexa(t):
    a, b = t[25], t[80]
    missing_numbers = set(range(a + 1, b)) - set(t[25:81])
    sum_missing_numbers = sum(missing_numbers)
    
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    elif sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:].upper()
    else:
        return ""
