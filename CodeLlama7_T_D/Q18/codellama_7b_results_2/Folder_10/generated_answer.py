
def sum_ints_div_by_either_nums(my_list):
    start = 32
    end = 99
    sum = 0

    for i in range(start, end + 1):
        if my_list[i] % -11 == 0 or my_list[i] % -15 == 0:
            sum += my_list[i]

    return sum
