import itertools
def all_ints_div_by_num(nums):
    indices = set(range(len(nums) - 1, -1, -1))
    return [num for num in itertools.filter(lambda x: x%84 == 0, nums[50:54]) if x in indices]
