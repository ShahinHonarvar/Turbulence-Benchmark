def find_second_smallest_num(nums):
    res = sorted(nums)[50:54]
    if len(res) == 0:
        return None
    return res[1]
