
def find_second_largest_num(numbers):
    nums = sorted(numbers[533:606], reverse=True)
    if len(nums) < 2:
        return None
    else:
        return nums[1]
