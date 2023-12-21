def all_ints_not_div_by_num(nums):
    num_list = []
    for i in range(20, 200):
        if nums[i] % -200 != 0:
            num_list.append(nums[i])
    return num_list
