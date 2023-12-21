def if_perfect_num(nums):
    return all(x == 2 * x - 1 for x in range(1, int(nums[77] ** .5) + 1))
