
def return_binary_or_hexa(tuple_int):
    a, b = tuple_int[86], tuple_int[99]
    sum_not_present = sum([i for i in range(a + 1, b) if i not in tuple_int[86:100]])
    if sum_not_present == 0:
        return ""
    elif sum_not_present % 2 == 0:
        return hex(sum_not_present)[2:]
    else:
        return bin(sum_not_present)[2:]
