
def return_binary_or_hexa(tuple):
    a = tuple[13]
    b = tuple[35]
    
    sum = 0
    for i in range(a+1, b):
        if i not in tuple[13:35]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
