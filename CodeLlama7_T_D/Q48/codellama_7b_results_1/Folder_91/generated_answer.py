 def return_binary_or_hexa(tuple):
    a = tuple[0]
    b = tuple[6]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
