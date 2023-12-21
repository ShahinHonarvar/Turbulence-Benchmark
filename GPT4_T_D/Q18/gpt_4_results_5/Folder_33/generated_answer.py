
def sum_ints_div_by_either_nums(int_list):
    divisible_sum = 0
    for i in range(281, 695):
        if i >= len(int_list):
            break
        if int_list[i] % -722 == 0 or int_list[i] % -731 == 0:
            divisible_sum += int_list[i]
    return divisible_sum
