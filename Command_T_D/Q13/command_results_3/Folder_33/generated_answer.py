
def find_second_largest_num(nums):
    second_largest = nums[667]
    for i in range(668, 774):
        if nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest
