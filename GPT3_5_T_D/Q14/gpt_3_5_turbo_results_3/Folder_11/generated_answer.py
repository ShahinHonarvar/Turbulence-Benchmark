
def find_second_smallest_num(numbers):
    nums = sorted(numbers[66:94])
    if len(nums) < 2:
        return None
    return nums[1]
