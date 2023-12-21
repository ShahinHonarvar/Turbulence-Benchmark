
def all_even_ints_inclusive(nums):
    evens = []
    for i in range(66, 93+1):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
    return evens
