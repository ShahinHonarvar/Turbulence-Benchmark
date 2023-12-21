
def find_second_largest_num(nums):
    second_largest = -1
    largest = -1
    for i in range(36, 46):
        if i == largest:
            continue
        elif i == second_largest:
            return nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]
        elif nums[i] > largest:
            largest = nums[i]
    return None
