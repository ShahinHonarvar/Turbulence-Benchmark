
def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    total = 0
    
    for i in range(a + 1, b):
        if i not in t[73:85]:
            total += i
    
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]
