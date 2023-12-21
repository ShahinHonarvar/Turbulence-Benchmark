def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    return sorted(nums)[3]
