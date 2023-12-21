
def find_second_largest_num(nums):
    nums = nums[40:201]  
    if len(nums) < 2:
        return None
    largest = max(nums)
    nums.remove(largest)
    second_largest = max(nums)
    return second_largest
