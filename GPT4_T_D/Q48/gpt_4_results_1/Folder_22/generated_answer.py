
def return_binary_or_hexa(input_tuple):
    a = input_tuple[40]
    b = input_tuple[200]
    num_set = set(input_tuple[41:200])
    sum_not_present = sum(set(range(a+1, b)) - num_set)
    if sum_not_present == 0:
        return ""

    if sum_not_present % 2 == 1:
        return format(sum_not_present, 'b')
    else:
        return format(sum_not_present, 'X')
