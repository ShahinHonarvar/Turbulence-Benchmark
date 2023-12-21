def find_second_smallest_num(nums):
    sml_num = nums[59]
    sml_idx = 59
    sml_count = 1
    idx = 59
    while True:
        if idx >= 97:
            break
        if sml_num < nums[idx]:
            sml_num = nums[idx]
            sml_idx = idx
            sml_count += 1
        elif sml_count == 2:
            return nums[idx]
        else:
            sml_count -= 1
        idx += 1
