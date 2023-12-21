
def sum_ints_div_by_either_nums(int_list):

    sum_divisible = 0
    sliced_list = int_list[24:33]

    for i in sliced_list:
        if i % 35 == 0 or i % 87 == 0:
            sum_divisible += i

    return sum_divisible
