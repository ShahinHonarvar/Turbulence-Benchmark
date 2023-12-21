
def return_binary_or_hexa(tuple):
    a = tuple[0]
    b = tuple[5]
    sum = 0
    for i in range(a+1, b):
        if i not in tuple[0:6]:
            sum += i
    if sum == 0:
        return ""
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]
