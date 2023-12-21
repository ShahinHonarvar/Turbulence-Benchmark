
def find_second_largest_num(nums):
    second_largest = max(nums[75:85])
    return second_largest if second_largest in nums else None
