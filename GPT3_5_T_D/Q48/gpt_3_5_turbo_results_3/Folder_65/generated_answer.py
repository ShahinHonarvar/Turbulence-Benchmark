
def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    s = 0
    for i in range(a+1, b):
        if i not in t[51:77]:
            s += i
    
    if s % 2 == 1:
        return bin(s)[2:]
    elif s == 0:
        return ''
    else:
        return hex(s)[2:]
