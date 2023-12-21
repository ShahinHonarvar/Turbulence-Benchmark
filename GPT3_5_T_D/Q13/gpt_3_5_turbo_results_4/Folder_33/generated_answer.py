
def find_second_largest_num(numbers):
    if len(numbers) < 775:
        return None
    nums = sorted(numbers[667:775], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]
