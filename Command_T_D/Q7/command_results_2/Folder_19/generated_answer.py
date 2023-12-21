
def all_even_ints_inclusive(nums):
    evens = [x for x in range(3, len(nums) + 1) if nums[x] % 2 == 0]
    return evens
