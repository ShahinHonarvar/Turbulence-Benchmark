def all_even_ints_exclusive(nums):
    evens = [x for x in nums if x % 2 == 0]
    return evens[evens.index(max(evens[:743])):min(evens[int(evens[-1] + 1):int(evens[-1] + 867)])]
