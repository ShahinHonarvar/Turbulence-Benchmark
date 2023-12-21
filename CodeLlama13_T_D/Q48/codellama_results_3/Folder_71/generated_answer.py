
def return_binary_or_hexa(tuple):
    a = tuple[20]
    b = tuple[35]
    sum = 0
    for i in range(a+1, b-1):
        if i not in tuple:
            sum += 1
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper()[2:]
