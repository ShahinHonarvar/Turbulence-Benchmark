def find_second_smallest_num(nums):
    res = sorted(nums)[66:93]
    if len(res) < 2:
        return None
    return res[-2]
