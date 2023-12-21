
def find_second_largest_num(nums):
    second_largest = sorted(nums)[62]
    for i in range(63, 78):
        if nums[i] > second_largest:
            second_largest = nums[i]
            break
    return second_largest
