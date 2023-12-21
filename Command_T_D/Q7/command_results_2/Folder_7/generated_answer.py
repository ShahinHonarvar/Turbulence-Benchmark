
def all_even_ints_inclusive(nums):
    evens = []
    for i in range(661, 924):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
    return evens
