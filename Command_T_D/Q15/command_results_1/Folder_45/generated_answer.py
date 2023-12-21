def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(30, 201) if i%2!=0)
