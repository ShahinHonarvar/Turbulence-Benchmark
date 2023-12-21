
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[1]
    b = tuple_of_integers[8]
    missing_nums = set(range(a + 1, b)) - set(tuple_of_integers[1:9])
    sum_output = sum(missing_nums)
    if sum_output == 0:
        return ''
    elif sum_output % 2 == 1:
        return bin(sum_output)[2:]
    else:
        return hex(sum_output)[2:].upper()
