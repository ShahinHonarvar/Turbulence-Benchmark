def find_second_smallest_num(nums):
    return next((x for x in sorted(set(range(40, 200 + 1)) if x in nums), key=lambda x: nums.index(x))), None)
