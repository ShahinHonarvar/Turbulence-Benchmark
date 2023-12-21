
def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]
    missing_numbers = set(range(a + 1, b)) - set(t[1:3])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:  
        return bin(sum_missing_numbers)[2:]
    else: 
        return hex(sum_missing_numbers)[2:].upper()
