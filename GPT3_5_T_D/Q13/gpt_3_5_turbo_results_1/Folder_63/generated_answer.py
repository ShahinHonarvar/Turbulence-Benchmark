
def find_second_largest_num(numbers):
    nums = numbers[22:89]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    else:
        return nums[1]
