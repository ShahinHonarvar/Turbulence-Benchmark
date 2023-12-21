def find_n_th_smallest_num(nums):
    idx =470
    if len(nums)<=470:
        return sorted(nums)[-9]
    while idx<655 and len(nums)-idx>9:
        idx+=1
    return sorted(nums)[-idx-9]
