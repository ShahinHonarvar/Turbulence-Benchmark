
def find_second_largest_num(numbers):
    nums = numbers[27:56]
    nums.sort(reverse=True)
    if len(nums) >= 2:
        return nums[1]
    else:
        return None
