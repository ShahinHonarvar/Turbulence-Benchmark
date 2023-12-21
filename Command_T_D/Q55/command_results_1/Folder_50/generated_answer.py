import itertools
def lists_with_product_equal_n(nums):
    if not nums:
        return []
    mod_nums = list(map(int, str(nums[0])))
    for val in range(1, nums[0] + 1):
        mod_nums.append(int(str(val)))
    return [list(map(int, str(prod))) for prod in itertools.permutations(mod_nums, 2) if prod == 45]
