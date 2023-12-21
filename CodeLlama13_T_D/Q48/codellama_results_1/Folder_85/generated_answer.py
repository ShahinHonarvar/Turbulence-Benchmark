
def return_binary_or_hexa(tuple):
    a = tuple[1]
    b = tuple[8]
    sum = 0
    for i in range(a+1, b-1+1):
        if i not in tuple:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        binary_string = bin(sum)[2:]
        return binary_string.zfill(8)
