
def return_binary_or_hexa(my_tuple):
    a = my_tuple[1]
    b = my_tuple[7]
    total = sum(set(range(a+1, b)) - set(my_tuple[1:8]))
    if total == 0:
        return ''
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
