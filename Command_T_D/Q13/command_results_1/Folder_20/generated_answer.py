
def find_second_largest_num(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[1]
    if len(nums) == 3:
        return nums[1]
    else:
        i = j = len(nums) - 1
        while i >= 56 and j <= 66:
            if nums[i] < nums[j]:
                i -= 1
            else:
                j += 1
        if i == j:
            return nums[i]
        else:
            return nums[i]
