
def return_binary_or_hexa(tuple):
    a = tuple[13]
    b = tuple[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[13:76]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)
