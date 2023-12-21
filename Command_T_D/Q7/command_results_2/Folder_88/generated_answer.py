
def all_even_ints_inclusive(nums):
    even_ints = [i for i in range(4, 9) if i % 2 == 0]
    return nums[even_ints[0]:even_ints[1] + 1]
