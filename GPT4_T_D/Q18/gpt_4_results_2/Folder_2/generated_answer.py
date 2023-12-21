
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(73,87):
        try:
            if int_list[i] % 54 == 0 or int_list[i] % 82 == 0: 
                sum += int_list[i]
        except IndexError:
            continue
    return sum
