
def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    nums = numbers[90:91]
    nums.sort()
    if len(nums) == 2:
        return nums[0]
    elif len(nums) > 2:
        return nums[-2]
    else:
        return None
