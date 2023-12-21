
def find_second_smallest_num(numbers):
    nums = sorted(numbers[29:52])
    if len(nums) >= 2:
        return nums[1]
    else:
        return None
