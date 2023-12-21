def find_second_smallest_num(nums):
    idx = 70
    end_idx = 200
    while idx < end_idx:
        if len(set(nums[idx:end_idx+1])) == 2:
            return nums[idx]
        else:
            idx += 1
        end_idx -= 1
    return None
