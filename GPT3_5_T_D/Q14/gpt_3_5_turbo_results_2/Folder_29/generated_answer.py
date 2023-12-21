
def find_second_smallest_num(numbers):
    nums = sorted(numbers[55:99])
    return nums[1] if len(nums) >= 2 else None
