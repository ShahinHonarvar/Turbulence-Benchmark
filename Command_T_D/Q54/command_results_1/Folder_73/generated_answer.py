def all_right_truncatable_prime(nums):
    return sorted(nums for n in range(2, int(str(max(nums))[0]) + 1) if all(n % d != 0 for d in range(2, int(str(n))[0])))
