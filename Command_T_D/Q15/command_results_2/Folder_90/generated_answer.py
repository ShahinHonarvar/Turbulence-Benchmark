def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(max(set(range(263, 747)))))
