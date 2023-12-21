
def return_binary_or_hexa(mytuple):
    a = mytuple[29] + 1
    b = mytuple[53] - 1
    sum = 0
    
    for i in range(a, b+1):
        if not i in mytuple:
            sum += i
            
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
