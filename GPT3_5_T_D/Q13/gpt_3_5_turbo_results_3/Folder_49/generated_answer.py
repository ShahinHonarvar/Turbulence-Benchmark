
def find_second_largest_num(numbers):
    nums = sorted(numbers[80:201])
    return nums[-2] if len(nums) >= 2 else None
