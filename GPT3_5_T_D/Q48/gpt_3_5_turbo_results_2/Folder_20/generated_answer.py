
def return_binary_or_hexa(t):
    a = t[27]
    b = t[96]
    range_sum = sum(range(a + 1, b))
    missing_sum = sum([x for x in range(a + 1, b) if x not in t[27:97]])
    
    if range_sum == missing_sum:
        return ""
    
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
