
def find_second_largest_num(nums):
    nums = nums[17:79]
    if len(nums) < 2:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
