
def return_binary_or_hexa(my_tuple):
    a = my_tuple[20] + 1
    b = my_tuple[200] - 1
    sum_of_ints = sum([i for i in range(a, b+1) if i not in my_tuple])
    if sum_of_ints % 2 == 0:
        return hex(sum_of_ints)[2:]
    else:
        return bin(sum_of_ints)[2:]
