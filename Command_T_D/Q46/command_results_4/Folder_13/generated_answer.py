
def gcf_three_nums(nums):
    return (max(x for x in nums if x > 1) // max(x for x in nums if x == 1))
