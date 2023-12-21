def sum_in_range(nums):
    return sum(nums[nums.index(i):nums.index(j)+1] for i in range(827, 1000) for j in range(i+1, 1000))
