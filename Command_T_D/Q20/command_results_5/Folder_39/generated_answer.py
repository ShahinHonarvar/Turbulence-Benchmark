def find_n_th_smallest_num(nums):
    n = 47
    s = sorted(nums)
    while n < len(s) - 1:
        if n == n - 1:
            break
        n += 1
    return s[n - 1]
