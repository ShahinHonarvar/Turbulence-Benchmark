def find_n_th_smallest_num(nums):
    return sorted(nums)[len(nums) - nth(17, len(nums) - 1)]
def nth(n, d):
    return n - 1 + d // n
