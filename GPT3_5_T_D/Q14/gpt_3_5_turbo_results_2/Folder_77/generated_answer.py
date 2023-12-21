
def find_second_smallest_num(numbers):
    nums = numbers[639:976]
    nums.sort()
    if len(nums) > 1:
        return nums[1]
    else:
        return None
