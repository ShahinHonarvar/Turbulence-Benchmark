def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    res = sorted(nums)[1]
    return res
