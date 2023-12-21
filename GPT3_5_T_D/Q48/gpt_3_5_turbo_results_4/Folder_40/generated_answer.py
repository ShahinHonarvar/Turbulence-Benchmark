
def return_binary_or_hexa(t):
    a = t[0]
    b = t[3]
    total_sum = sum([x for x in range(a + 1, b) if x not in t])
    
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    elif total_sum == 0:
        return ""
    else:
        return format(total_sum, 'X')
