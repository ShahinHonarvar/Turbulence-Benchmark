def find_second_smallest_num(nums):
    result = sorted(nums)[75:88]
    if len(result) < 2:
        return None
    return result[1]
