
def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) <= 2:
        return None
    else:
        second_largest = nums[1]
        for i in range(2, len(nums)):
            if nums[i] > second_largest:
                second_largest = nums[i]
        return second_largest
