
def return_binary_or_hexa(tuple):
    a = tuple[50]
    b = tuple[200]
    sum = 0
    for i in range(a+1,b-1):
        if i not in tuple:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
