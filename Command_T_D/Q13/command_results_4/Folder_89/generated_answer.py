
def find_second_largest_num(nums):
    if len(nums) < 57 or len(nums) > 83:
        return None
    sm, second_largest_num = sorted(nums)[56], sorted(nums)[-2]
    return second_largest_num if sm <= second_largest_num <= nums[-1] else None
