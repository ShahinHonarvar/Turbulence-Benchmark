
def find_second_smallest_num(numbers):
    nums = numbers[4:5]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[1]
