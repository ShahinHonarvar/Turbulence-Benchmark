
def all_even_ints_exclusive(nums):
    exclusive_evens = []
    for i in range(362, 643):
        if nums[i] % 2 == 0:
            exclusive_evens.append(nums[i])
    return exclusive_evens
