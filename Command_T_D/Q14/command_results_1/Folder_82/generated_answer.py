def find_second_smallest_num(nums):
    res = sorted(nums)[20:200]
    if len(res) == 0:
        return None
    return res[1]
