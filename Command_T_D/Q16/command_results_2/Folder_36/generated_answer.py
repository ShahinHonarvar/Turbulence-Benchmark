def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    even_nums = [x for x in nums if x % 2 == 0]
    if not even_nums:
        return 0
    return sum(even_nums[246:750])
