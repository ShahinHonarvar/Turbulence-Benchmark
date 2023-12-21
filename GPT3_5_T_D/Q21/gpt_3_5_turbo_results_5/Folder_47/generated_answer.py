
def all_ints_div_by_num(nums):
    divisible_nums = []
    for i in range(75, 89):
        if i < len(nums) and nums[i] % -27 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums
