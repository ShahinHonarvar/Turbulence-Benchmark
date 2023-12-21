
def find_second_largest_num(nums):
    nums = nums[533:606]
    if len(nums) < 2:
        return None
    largest = max(nums[0], nums[1])
    second_largest = min(nums[0], nums[1])
    for num in nums[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
