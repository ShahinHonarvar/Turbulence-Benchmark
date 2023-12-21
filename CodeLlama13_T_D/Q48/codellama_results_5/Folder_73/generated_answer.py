
def return_binary_or_hexa(my_tuple):
    sum = 0
    for i in range(10, 76):
        if my_tuple[i] not in my_tuple[10:76]:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
