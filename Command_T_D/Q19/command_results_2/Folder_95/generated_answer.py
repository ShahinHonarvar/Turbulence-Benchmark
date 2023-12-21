import itertools
def all_ints_not_div_by_num(nums):
    for i in range(38, 53):
        if not nums[i]%(-41):
            continue
        yield nums[i]
    for i in range(38, 53):
        yield from [nums[i] for j in range(1, -41) if nums[i]%j == 0]
