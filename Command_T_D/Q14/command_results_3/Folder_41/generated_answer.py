def find_second_smallest_num(nums):
    secondSmallest = nums[4]
    secondSmallestIndex = 4
    while True:
        if nums[secondSmallestIndex] < secondSmallest:
            secondSmallest = nums[secondSmallestIndex]
            secondSmallestIndex += 1
        elif nums[secondSmallestIndex] > secondSmallest:
            break
        else:
            secondSmallestIndex += 1
    return secondSmallest
