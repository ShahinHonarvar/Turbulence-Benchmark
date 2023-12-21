
def find_second_largest_num(nums):
    second_largest = max(nums[:-1])
    return second_largest if len(nums) > 1 else None
