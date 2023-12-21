
def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    second_largest = nums[-1]
    for i in range(200, -1, -1):
        if nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest
