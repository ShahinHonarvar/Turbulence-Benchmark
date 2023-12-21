
def return_binary_or_hexa(my_tuple):
    a = my_tuple[3] + 1
    b = my_tuple[9] - 1
    sum_of_ints = sum(set(range(a, b + 1)) - set(my_tuple[3:9]))
    if sum_of_ints % 2 == 0:
        return hex(sum_of_ints)[2:]
    else:
        return bin(sum_of_ints).replace('0b', '')
