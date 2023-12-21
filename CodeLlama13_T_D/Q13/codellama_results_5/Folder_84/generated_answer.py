
def find_second_largest_num(nums):
    largest = None
    second_largest = None
    for i in range(43, 87):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest
