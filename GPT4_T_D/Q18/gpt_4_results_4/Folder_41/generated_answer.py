
def sum_ints_div_by_either_nums(int_list):
    sum_of_numbers = 0
    for i in range(10):
        if int_list[i] % 6 == 0 or int_list[i] % -3 == 0:
            sum_of_numbers += int_list[i]
    return sum_of_numbers
