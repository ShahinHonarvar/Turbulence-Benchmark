
def return_binary_or_hexa(tuple):
    a = tuple[37] + 1
    b = tuple[43] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in tuple:
            sum += i
    if sum % 2 == 0:
        return format(sum, 'x')
    else:
        return bin(sum)[2:]
