
def all_ints_div_by_both_two_nums(nums_list):
    try:
        range_nums = nums_list[0:2]
        divisible_nums = [num for num in range_nums if num % 2 == 0 and num % 1 ==0]
        return divisible_nums
    except:
        return []
