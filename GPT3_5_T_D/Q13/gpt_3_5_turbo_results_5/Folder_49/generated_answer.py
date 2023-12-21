
def find_second_largest_num(numbers):
    nums = sorted(numbers[80:201], reverse=True)
    return nums[1] if len(nums) > 1 else None
