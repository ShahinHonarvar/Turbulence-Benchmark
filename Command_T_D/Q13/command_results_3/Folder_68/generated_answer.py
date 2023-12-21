
def find_second_largest_num(nums):
    second_largest_num = max(nums[:8])
    return second_largest_num if second_largest_num in nums else None
