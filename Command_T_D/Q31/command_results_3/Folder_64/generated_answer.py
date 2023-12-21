def if_perfect_num(nums):
    return all(str(x).count(".") == 1 for x in nums)
