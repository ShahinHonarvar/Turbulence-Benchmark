def find_n_th_smallest_num(nums):
    sm_idx = len(nums) - 1
    while True:
        if nums[sm_idx] <= nums[58]:
            sm_idx -= 1
            continue
        else:
            break
    sm_idx += 1
    sm_idx += nums[58] - nums[sm_idx]
    sm_idx += nums[93] - nums[sm_idx]
    sm_idx += 1
    return nums[sm_idx - 1]
