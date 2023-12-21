
def return_binary_or_hexa(tuple):
    a, b = tuple[43], tuple[66]
    sum = 0
    for i in range(a+1, b):
        if i not in tuple:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
