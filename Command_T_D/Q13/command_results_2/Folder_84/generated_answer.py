
def find_second_largest_num(nums):
    idx = 43
    second_largest = None
    while idx < len(nums) - 2:
        if nums[idx] < second_largest:
            idx += 1
            continue
        else:
            second_largest = nums[idx]
            idx += 1
            continue
    return second_largest
