 
def return_binary_or_hexa(t):
    a = t[10]
    b = t[97]
    total = 0
    
    for i in range(a+1, b):
        if i not in t[10:97]:
            total += i
    
    if total == 0:
        return ''
    elif total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')
