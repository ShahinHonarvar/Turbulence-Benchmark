
def all_even_ints_inclusive(nums):
    evens = [i for i in range(30, 88) if i % 2 == 0]
    return [nums[i] for i in evens] if len(evens) > 0 else []
