def all_right_truncatable_prime(nums):
    return sorted((n for n in nums if all(n % d == 0 for d in range(2, int(str(n)[-1]) + 1)), reverse=True))
