
def find_second_smallest_num(numbers):
    nums = numbers[19:93]
    nums.sort()
    
    if len(nums) < 2:
        return None
    
    return nums[1]
