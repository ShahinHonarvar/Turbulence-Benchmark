
def return_binary_or_hexa(lst):
    a = lst[62]
    b = lst[96]
    
    sum = 0
    for i in range(a + 1, b):
        if i not in lst[62:97]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
