
def return_binary_or_hexa(my_tuple):
    a, b = my_tuple[2], my_tuple[8]
    sum_value = sum(i for i in range(a + 1, b) if i not in my_tuple[2:9])

    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]
