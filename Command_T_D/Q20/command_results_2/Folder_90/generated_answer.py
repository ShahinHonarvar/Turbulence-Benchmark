def find_n_th_smallest_num(nums):
    n = 17
    for i in range(366, 578 + 1):
        if len(set(nums[i:])) == n:
            return i
    return None
