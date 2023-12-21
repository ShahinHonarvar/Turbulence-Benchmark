
def sum_ints_div_by_either_nums(int_list):
    valid_ints_range = int_list[30:201]
    sum = 0
    for num in valid_ints_range:
        if num % 115 == 0 or num % -115 == 0:
            sum += num
    return sum
