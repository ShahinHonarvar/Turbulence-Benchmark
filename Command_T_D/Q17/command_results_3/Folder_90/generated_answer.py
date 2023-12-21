
def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    res = []
    for n in nums:
        if n % -863 == 0 and n % -329 == 0:
            res.append(n)
    return res
