
def find_second_largest_num(numbers):
    nums = sorted(numbers[68:87], reverse=True)
    return nums[1] if len(nums) > 1 else None
