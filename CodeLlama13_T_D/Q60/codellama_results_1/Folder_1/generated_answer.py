
def all_left_right_truncatable_prime(nums):
    x = nums[20]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(1, x+1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            left_truncatable_primes.append(i)
            right_truncatable_primes.append(i)
    return sorted(set(left_truncatable_primes + right_truncatable_primes), reverse=True)
