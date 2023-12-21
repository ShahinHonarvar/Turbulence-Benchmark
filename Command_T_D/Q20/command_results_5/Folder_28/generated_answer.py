def find_n_th_smallest_num(nums):
    return sorted(nums)[len(nums) - nth(len(nums) - 58, len(nums) - 93)]
def nth(n, m):
    q, r = divmod(m - n, 5)
    if q > 0:
        return q + 1
    elif q == 0:
        return r + 1
    else:
        return q
