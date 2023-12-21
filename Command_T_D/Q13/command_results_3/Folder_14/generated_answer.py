
def find_second_largest_num(nums):
    idx = 5
    end = nums[-1]
    while idx < end:
        mid = (idx + end) // 2
        if nums[mid] < nums[idx]:
            idx = mid
        else:
            end = mid
    return nums[idx] if idx <= 7 else None
