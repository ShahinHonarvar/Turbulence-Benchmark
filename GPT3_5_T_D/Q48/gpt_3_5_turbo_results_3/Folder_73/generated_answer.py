
def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    total = 0
    for i in range(a+1, b):
        if i not in t[10:76]:
            total += i
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
