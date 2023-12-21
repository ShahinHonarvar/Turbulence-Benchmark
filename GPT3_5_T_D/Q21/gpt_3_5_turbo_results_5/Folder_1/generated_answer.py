
def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[59:78]:
        if num % (-95) == 0:
            divisible_nums.append(num)
    return divisible_nums
