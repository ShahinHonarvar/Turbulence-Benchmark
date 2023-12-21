
def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(41, 57):
        if i < len(int_list):
            if int_list[i] % 82 == 0 or int_list[i] % 90 == 0:
                total += int_list[i]
    return total
