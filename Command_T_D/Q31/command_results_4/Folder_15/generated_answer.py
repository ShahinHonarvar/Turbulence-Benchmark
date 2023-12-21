def if_perfect_num(nums):
    return all(str(x) == '0' for x in nums[:10]) and nums[10] == 2 * sum(nums[0:10])
