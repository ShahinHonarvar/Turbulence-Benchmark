
def return_binary_or_hexa(tuple):
    a = tuple[56] + 1
    b = tuple[90] - 1
    sum = 0
    for i in range(a, b+1):
        if not i in tuple:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
