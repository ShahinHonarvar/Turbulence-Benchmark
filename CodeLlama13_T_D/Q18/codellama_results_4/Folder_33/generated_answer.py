
def sum_ints_div_by_either_nums(my_list):
    start = 281
    end = 694
    sum = 0
    for i in range(start, end+1):
        if my_list[i] % -722 == 0 or my_list[i] % -731 == 0:
            sum += my_list[i]
    return sum
