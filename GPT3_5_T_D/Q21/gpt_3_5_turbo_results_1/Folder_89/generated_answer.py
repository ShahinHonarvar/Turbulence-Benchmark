
def all_ints_div_by_num(nums):
    divisible_nums = []
    for i in range(30, 60):
        if i < len(nums) and nums[i] % 39 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums
