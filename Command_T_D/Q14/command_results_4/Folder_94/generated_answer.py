def find_second_smallest_num(nums):
    secondSmallestNum = next((el for el in range(len(nums) - 52, len(nums) - 71) if nums[el] < min(nums[52:71])), None)
    return nums[secondSmallestNum]
