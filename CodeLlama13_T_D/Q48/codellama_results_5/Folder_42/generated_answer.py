
def return_binary_or_hexa(my_tuple):
    sum = 0
    for i in range(18, 60):
        if my_tuple[i] not in my_tuple[18:60]:
            sum += my_tuple[i]
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
