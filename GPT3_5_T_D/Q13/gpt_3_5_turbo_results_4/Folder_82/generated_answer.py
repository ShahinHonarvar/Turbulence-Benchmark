
def find_second_largest_num(numbers):
    nums = sorted(numbers[20:201], reverse=True)
    if len(nums) > 1:
        return nums[1]
    else:
        return None
