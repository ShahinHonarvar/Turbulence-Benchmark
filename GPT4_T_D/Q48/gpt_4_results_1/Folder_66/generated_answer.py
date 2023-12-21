
def return_binary_or_hexa(int_tuple):
    a = int_tuple[11]
    b = int_tuple[76]
    sum_ints = sum(set(range(a + 1, b)) - set(int_tuple[11:77]))
    if sum_ints == 0:
        return ''
    if sum_ints % 2 == 0:
        return hex(sum_ints)[2:]
    else:
        return bin(sum_ints)[2:]
