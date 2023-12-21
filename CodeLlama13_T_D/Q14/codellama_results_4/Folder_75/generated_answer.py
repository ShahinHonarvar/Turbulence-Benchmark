
def find_second_smallest_num(nums):
    if len(nums) <= 1:
        return None
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[12]
    for i in range(13, 92 + 1):
        if sorted_nums[i] < second_smallest:
            second_smallest = sorted_nums[i]
    return second_smallest
