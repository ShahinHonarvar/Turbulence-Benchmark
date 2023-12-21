
def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    
    used = set(t[21:35])
    all_numbers = set(range(a + 1, b))
    
    missing_numbers = all_numbers.difference(used)
    
    s = sum(missing_numbers)
    
    if s == 0:
        return ""
        
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()
