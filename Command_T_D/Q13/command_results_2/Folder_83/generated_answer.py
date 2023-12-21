
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        largest = max(nums)
        j = 0
        while True:
            if largest == nums[j]:
                j += 1
            else:
                break
            if j == len(nums):
                break
            largest = nums[j]
            j += 1
        return nums[j - 1]
