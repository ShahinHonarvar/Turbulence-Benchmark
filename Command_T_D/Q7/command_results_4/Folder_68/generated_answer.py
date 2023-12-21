
def all_even_ints_inclusive(nums):
    evens = [x for x in range(0, len(nums) + 1) if nums[x] % 2 == 0]
    return evens[1:-1] if len(evens) > 0 else []
