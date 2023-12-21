def all_left_truncatable_prime(nums):
    return sorted(nums for num in nums if all(num % d == 0 or num % d == d for d in range(2, int(num ** 0.5) + 1)))
