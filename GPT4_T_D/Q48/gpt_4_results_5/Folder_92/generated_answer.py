
def return_binary_or_hexa(tuple):
    a, b = tuple[0], tuple[2]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i
    if sum == 0:
        return ""
    elif sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
