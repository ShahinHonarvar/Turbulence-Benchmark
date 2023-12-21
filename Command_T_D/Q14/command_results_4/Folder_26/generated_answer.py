def find_second_smallest_num(nums):
    secondSmallest = float('inf')
    secondSmallestIndex = -1
    for i in range(len(nums)):
        if nums[i] < secondSmallest:
            secondSmallest = nums[i]
            secondSmallestIndex = i
    if secondSmallestIndex == -1:
        return None
    return nums[secondSmallestIndex]
