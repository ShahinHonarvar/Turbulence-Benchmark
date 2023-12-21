
def sum_ints_div_by_either_nums(num_list):
    sum_nums = 0
    for i in range(10):
        if num_list[i]%10 == 0 or num_list[i]%100 == 0:
            sum_nums += num_list[i]
    return sum_nums
