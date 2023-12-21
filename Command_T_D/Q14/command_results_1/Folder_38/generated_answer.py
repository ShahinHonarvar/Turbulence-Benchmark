def find_second_smallest_num(nums):
    secondSmallestNum = None
    for i in range(len(nums)-5, len(nums)-2):
        if len(nums) == i + 2:
            continue
        if nums[i] < nums[i + 1]:
            secondSmallestNum = nums[i]
    return secondSmallestNum
