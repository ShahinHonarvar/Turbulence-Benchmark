def find_second_smallest_num(nums):
    second_smallest = nums[23]
    i = 23
    while i >= 1 and second_smallest >= nums[i - 1]:
        second_smallest = nums[i - 1]
        i -= 1
    return second_smallest
