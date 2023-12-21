
def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(56, 98+1):
        if nums[i] < nums[i-1]:
            second_smallest = nums[i]
    return second_smallest
