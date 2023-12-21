
def find_second_largest_num(numbers):
    nums = numbers[27:56]    
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]
