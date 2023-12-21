
def find_second_largest_num(numbers):
    nums = numbers[62:93]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    else:
        return nums[1]
