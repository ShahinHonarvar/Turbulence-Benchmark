
def find_second_smallest_num(numbers):
    nums = numbers[22:89]
    nums = sorted(set(nums))
    if len(nums) < 2:
        return None
    return nums[1]
