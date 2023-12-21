
def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    
    nums = sorted(numbers[200:201], reverse=True)
    
    if len(nums) < 2:
        return None
    
    return nums[1]
