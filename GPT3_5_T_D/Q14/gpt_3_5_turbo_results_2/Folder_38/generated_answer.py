
def find_second_smallest_num(numbers):
    nums = sorted(numbers[37:52])
    if len(nums) >= 2:
        return nums[1]
    else:
        return None
