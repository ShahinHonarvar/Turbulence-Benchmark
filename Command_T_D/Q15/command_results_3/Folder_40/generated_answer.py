def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(0,len(nums)-1) if i%2!=0)
