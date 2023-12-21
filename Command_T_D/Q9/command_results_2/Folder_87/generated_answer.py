def all_odd_ints_inclusive(nums):
    return [nums[i] for i in range(len(nums)-2, -1, 2) if nums[i]%2!=0]
