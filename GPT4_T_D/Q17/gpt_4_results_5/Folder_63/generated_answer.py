
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[31:51] if num % 81 == 0 and num % 64 == 0]
    return divisible_nums
