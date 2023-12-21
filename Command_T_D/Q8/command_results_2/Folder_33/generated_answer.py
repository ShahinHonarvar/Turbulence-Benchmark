import bisect
def all_even_ints_exclusive(nums):
    if not nums:
        return []
    even_nums = sorted(set(nums[369:983]) & {x for x in range(369, 983) if x % 2 == 0})
    even_nums.sort()
    return even_nums
