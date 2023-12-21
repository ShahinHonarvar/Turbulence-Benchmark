def all_left_truncatable_prime(nums):
    return sorted(set(nums) - set(x for x in nums if not x.isprime()))
