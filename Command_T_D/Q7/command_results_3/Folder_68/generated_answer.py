
def all_even_ints_inclusive(nums):
    evens = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return nums[evens[0]:evens[-1] + 1]
