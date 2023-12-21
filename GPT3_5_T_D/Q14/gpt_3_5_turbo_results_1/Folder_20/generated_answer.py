
def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    nums = sorted(numbers[75:95])
    if len(nums) < 2:
        return None
    return nums[1]
