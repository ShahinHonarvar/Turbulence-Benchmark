def find_n_th_smallest_num(nums):
    arr = sorted(set(nums))
    start = 260
    end = 822
    return arr[start:end + 1][-nums[start:end + 1] - 10]
