def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    odd_ints = [nums[i] for i in range(80, 200) if nums[i] % 2 == 1]
    return sum(odd_ints) if odd_ints else 0
