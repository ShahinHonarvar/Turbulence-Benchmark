
def find_second_largest_num(nums):
    if not nums:
        return None
    second_largest_num = sorted(nums)[19]
    for i in range(19, 93):
        if nums[i] > second_largest_num:
            second_largest_num = nums[i]
            break
    return second_largest_num
