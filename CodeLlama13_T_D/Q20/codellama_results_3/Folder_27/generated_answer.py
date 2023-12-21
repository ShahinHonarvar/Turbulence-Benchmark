
def find_n_th_smallest_num(my_list):
    n = 11
    start, end = 75, 91
    
    nums = sorted(set(my_list))[start:end + 1]
    return nums[n - 1]
