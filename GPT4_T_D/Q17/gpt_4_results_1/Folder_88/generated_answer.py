
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[3:10] if num % 6 == 0 and num % 1 == 0]
    return divisible_nums
