
def sum_ints_div_by_either_nums(int_list):
    subtotal = 0
    for i in range(58, min(76, len(int_list))):
        if int_list[i] % 72 == 0 or int_list[i] % 62 == 0:
            subtotal += int_list[i]
    return subtotal
