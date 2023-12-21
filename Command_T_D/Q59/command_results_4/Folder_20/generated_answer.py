def all_left_truncatable_prime(nums):
    return sorted(nums for n in nums if n % 2 == 1 and n > 9 and all(int(d) for d in str(n) if d))
