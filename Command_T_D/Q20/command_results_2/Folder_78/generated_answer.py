def find_n_th_smallest_num(nums):
    n = len(nums)
    low = 16
    high = n - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] <= n:
            low = mid
        else:
            high = mid
    return nums[low]
