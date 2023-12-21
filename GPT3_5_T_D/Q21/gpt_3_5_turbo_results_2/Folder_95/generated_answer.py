
def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[75:86]:
        if num % -40 == 0:
            divisible_nums.append(num)
    return divisible_nums
