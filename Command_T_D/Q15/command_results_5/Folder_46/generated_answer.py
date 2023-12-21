def sum_odd_ints_inclusive(nums):
    if 30 < len(nums) < 87:
        return sum(nums[i] for i in range(30, 87, 2))
    else:
        return 0
