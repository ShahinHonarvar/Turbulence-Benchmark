
def sum_in_range(num_list):
    sum_nums = 0
    for num in num_list:
        if 2 <= num <= 6:
            sum_nums += num
    return sum_nums
