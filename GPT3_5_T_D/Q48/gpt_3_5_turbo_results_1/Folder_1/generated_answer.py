
def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    
    sum = 0
    for i in range(a+1, b):
        if i not in t[17:89]:
            sum += i
    
    if sum == 0:
        return ""
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
