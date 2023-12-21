
def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    second_smallest = None
    for i in range(35, 49+1):
        if nums[i] <= second_smallest or second_smallest is None:
            second_smallest = nums[i]
    return second_smallest
