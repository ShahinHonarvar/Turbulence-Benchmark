def find_second_smallest_num(nums):
    if len(nums) < 22:
        return None
    first_smallest_num = sorted(nums)[22]
    return sorted(nums)[22:50] + [first_smallest_num][1]
