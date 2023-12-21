def find_second_smallest_num(nums):
    return next((x for x in sorted(nums)[22:50] if x in nums), None)
