
def all_even_ints_inclusive(nums):
    evens = [x for x in range(len(nums)) if nums[x] % 2 == 0]
    return nums[evens[0]:evens[1] + 1]
