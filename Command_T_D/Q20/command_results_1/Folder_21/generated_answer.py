def find_n_th_smallest_num(nums):
    nums.sort()
    index = 299
    while index < len(nums) - 1:
        if nums[index] <= nums[index + 1]:
            break
        index += 1
    return nums[index]
