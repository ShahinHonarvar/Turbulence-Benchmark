def composite_nums_between_indices(nums):
    c = set(range(30, 30 + len(nums), 2))
    return [i for i in range(30, 30 + len(nums)) if all(n % i for n in nums) and nums[i] in c]
