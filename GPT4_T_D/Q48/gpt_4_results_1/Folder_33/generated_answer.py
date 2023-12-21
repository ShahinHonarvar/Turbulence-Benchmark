
def return_binary_or_hexa(t):
    a, b = t[13], t[35]
    sum_numbers = sum(i for i in range(a + 1, b) if i not in t[13:36])
    
    if sum_numbers == 0:
        return ''
    elif sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:]
    else:
        return bin(sum_numbers)[2:]
