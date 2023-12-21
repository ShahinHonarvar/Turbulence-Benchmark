def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    return sorted(nums)[1]
