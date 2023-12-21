
def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    integers = set(t[a+1:b])
    
    total = 0
    for i in range(a+1, b):
        if i not in integers:
            total += i
    
    if total == 0 or total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
