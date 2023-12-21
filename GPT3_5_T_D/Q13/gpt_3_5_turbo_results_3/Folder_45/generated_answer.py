
def find_second_largest_num(nums):
    nums = nums[30:201]
    if len(nums) < 2:
        return None
    largest = None
    second_largest = None
    for num in nums:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest
