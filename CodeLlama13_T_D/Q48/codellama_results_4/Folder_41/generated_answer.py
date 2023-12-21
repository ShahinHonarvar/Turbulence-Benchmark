
def return_binary_or_hexa(tuple):
    a = tuple[3] + 1
    b = tuple[8] - 1
    
    if len(list(set(range(a, b + 1)) - set(tuple))) == 0:
        return ''
    
    sum = 0
    for i in range(a, b + 1):
        if i not in tuple:
            sum += i
            
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
