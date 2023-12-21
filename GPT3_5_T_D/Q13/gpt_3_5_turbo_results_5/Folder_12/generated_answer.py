
def find_second_largest_num(numbers):
    if len(numbers) < 65:
        return None
    
    nums = numbers[14:65]
    nums.sort(reverse=True)
    
    if len(nums) < 2:
        return None
    
    return nums[1]
