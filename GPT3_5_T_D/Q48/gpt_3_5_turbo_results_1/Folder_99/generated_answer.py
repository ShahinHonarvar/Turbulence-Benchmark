
def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in t[427:670]:
            total_sum += i
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ""
    else:
        return hex(total_sum)[2:]
