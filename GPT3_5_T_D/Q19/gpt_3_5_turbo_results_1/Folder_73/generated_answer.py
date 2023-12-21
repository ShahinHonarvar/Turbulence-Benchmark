
def all_ints_not_div_by_num(nums):
    not_divisible_nums = []
    for num in nums[70:98]:
        if num % -88 != 0:
            not_divisible_nums.append(num)
    return not_divisible_nums
