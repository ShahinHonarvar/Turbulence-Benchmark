
def find_second_largest_num(nums):
    second_largest_num = None
    largest_num = max(nums)
    for i in range(74, 95 + 1):
        if largest_num in nums[i:]:
            second_largest_num = nums[i]
            break
    return second_largest_num
