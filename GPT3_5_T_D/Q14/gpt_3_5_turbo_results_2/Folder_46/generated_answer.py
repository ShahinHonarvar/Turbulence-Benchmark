
def find_second_smallest_num(numbers):
    nums = numbers[13:69]
    nums.sort()
    if len(nums) > 1:
        return nums[1]
    else:
        return None
