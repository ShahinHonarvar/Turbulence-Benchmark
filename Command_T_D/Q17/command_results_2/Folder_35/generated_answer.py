
import itertools

def all_ints_div_by_both_two_nums(nums):
    return [x for x in itertools.permutations(range(77, 87+1), 2) if all(nums[i]%d == 0 for i, d in enumerate(x))
