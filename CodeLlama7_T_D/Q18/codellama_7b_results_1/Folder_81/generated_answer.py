
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(10, 100 + 1):
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:
            sum += my_list[i]
    return sum
