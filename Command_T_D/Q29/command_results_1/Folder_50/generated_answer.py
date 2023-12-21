def gcf_two_nums(nums):
    return max(x // y for x, y in zip(nums[:90], nums[:54]))
