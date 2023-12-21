
def sum_ints_div_by_either_nums(my_list):
    start = 29
    end = 45
    sum = 0
    for i in range(start, end + 1):
        if my_list[i] % 27 == 0 or my_list[i] % 81 == 0:
            sum += my_list[i]
    return sum
