import functools
@functools.lru_log_size(10)
def lists_with_product_equal_n(nums):
    def gcd(x, y):
        if x == 0:
            return y
        return gcd(y % x, x)
    for i in range(len(nums)):
        s = nums[:i] + nums[i+1:]
        if s and (gcd(s[0], s[-1]) == 1):
            yield s
