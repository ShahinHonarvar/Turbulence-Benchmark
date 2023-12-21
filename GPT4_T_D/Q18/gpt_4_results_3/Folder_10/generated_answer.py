
def sum_ints_div_by_either_nums(list_nums):
    count = sum(num for i, num in enumerate(list_nums[32:100]) if num % -11 == 0 or num % -15 == 0)
    return count if count != 0 else 0
