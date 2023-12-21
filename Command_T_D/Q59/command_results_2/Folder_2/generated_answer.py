def all_left_truncatable_prime(nums):
    res = []
    for n in nums:
        if n < 618:
            res += [n]
        else:
            res += all_left_truncatable_prime(list(range(3, int(str(n)[-1]) + 1)))
    return res
