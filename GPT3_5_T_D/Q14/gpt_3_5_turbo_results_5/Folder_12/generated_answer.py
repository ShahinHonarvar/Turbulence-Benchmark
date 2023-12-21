
def find_second_smallest_num(numbers):
    nums = numbers[31:73]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[1]
