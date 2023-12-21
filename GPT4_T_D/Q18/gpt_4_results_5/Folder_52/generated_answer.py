
def sum_ints_div_by_either_nums(int_list):
    sum_of_ints = 0
    for num in int_list[48:60]:
        if num % 88 == 0 or num % 58 == 0:
            sum_of_ints += num
    return sum_of_ints
