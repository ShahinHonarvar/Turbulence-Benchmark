
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[138:425] if num % -863 == 0 and num % -329 == 0]
    return divisible_nums
