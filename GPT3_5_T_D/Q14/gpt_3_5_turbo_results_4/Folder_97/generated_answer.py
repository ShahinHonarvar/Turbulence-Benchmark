
def find_second_smallest_num(numbers):
    nums = numbers[31:35]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]
