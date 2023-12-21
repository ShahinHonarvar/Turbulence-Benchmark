def find_second_smallest_num(nums):
    result = sorted(nums)[1]
    if result == len(nums) - 1:
        return None
    return result
