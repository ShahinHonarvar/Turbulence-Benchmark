def all_left_truncatable_prime(nums):
    return sorted(nums for num in nums if num < 10**(len(str(num)) - 1) and all(int(d) for d in str(num)))
