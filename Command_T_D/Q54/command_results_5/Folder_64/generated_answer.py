def all_right_truncatable_prime(nums):
    x = nums[4]
    y = str(x)
    return sorted(list(filter(lambda x: x == int(y[:-1]), range(2, x + 1))))
