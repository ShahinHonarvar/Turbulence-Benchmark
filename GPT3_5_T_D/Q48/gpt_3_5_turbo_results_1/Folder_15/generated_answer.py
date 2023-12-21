
def return_binary_or_hexa(t):
    a = t[0]
    b = t[4]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in t[1:4]:
            total_sum += i
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
