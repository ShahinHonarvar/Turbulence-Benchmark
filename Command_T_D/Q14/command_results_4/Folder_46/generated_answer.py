def find_second_smallest_num(nums):
    if len(nums) <= 12:
        return None
    second_smallest_num = sorted(nums)[13]
    return second_smallest_num
