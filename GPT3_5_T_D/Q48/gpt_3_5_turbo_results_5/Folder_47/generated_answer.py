
def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    s = 0
    
    for i in range(a+1, b):
        if i not in t[29:54]:
            s += i
    
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
