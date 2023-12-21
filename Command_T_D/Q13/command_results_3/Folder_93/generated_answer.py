
def find_second_largest_num(nums):
    idx = 75
    end_idx = 94
    second_largest_num = None
    while idx < end_idx:
        if len(nums) == idx:
            break
        elif len(nums) == end_idx:
            return None
        second_largest_num = nums[idx]
        idx += 1
        end_idx -= 1
    return second_largest_num
