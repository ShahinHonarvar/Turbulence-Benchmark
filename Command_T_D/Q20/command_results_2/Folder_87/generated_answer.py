def find_n_th_smallest_num(nums):
    sml_nums = sorted(nums)[:nums.count(sml_nums[0])]
    sml_nums += sorted(nums)[nums.count(sml_nums[0]):]
    return sml_nums[55]
