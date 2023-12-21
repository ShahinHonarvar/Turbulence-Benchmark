def find_second_smallest_num(nums):
    if len(nums) < 11:
        return None
    return sorted(nums)[10]
