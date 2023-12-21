def find_second_smallest_num(nums):
    sm = sorted(nums)[1]
    return sm if len(nums) > 1 and sm in nums else None
