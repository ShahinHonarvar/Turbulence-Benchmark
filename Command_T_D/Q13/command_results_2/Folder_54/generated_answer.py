
def find_second_largest_num(nums):
    if len(nums) == 0:
        return None
    largest = max(nums)
    second = largest
    for i in range(33, 55):
        if nums[i] > second:
            second = nums[i]
    return second
