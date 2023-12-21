
import itertools

def sum_ints_div_by_either_nums(nums):
    for n in itertools.chain(nums[299:382:2], nums[301:383:2]):
        if n % 858 == 0 or n % 952 == 0:
            yield n
    return sum(nums[299:382:2] + nums[301:383:2])
