
def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    second_smallest = None
    for i in range(30, 201):
        num = nums[i]
        if second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
