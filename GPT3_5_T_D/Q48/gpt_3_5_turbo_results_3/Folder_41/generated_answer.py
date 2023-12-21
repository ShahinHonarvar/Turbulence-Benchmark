
def return_binary_or_hexa(tuple):
    a = tuple[3]
    b = tuple[8]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[3:9]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
