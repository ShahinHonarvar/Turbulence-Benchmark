def find_second_smallest_num(nums):
    res = None
    for i in range(82, 86):
        if len(nums) > i:
            res = sorted(nums)[i]
            break
    return res
