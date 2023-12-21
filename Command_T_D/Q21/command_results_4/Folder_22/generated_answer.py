def all_ints_div_by_num(nums):
    return [i for i in range(10, 10 + len(nums) - 1) if i % 10 == nums[i // 10]]
