
def return_binary_or_hexa(tuple):
    sum = 0
    for i in range(34, 69):
        if i+1 not in tuple:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
