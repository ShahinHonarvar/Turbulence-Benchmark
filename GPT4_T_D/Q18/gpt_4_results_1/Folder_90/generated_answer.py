
def sum_ints_div_by_either_nums(int_list):
    subset_list = int_list[138:425]
    sum = 0
    for num in subset_list:
        if num % -863 == 0 or num % -329 == 0:
            sum += num
    return sum
