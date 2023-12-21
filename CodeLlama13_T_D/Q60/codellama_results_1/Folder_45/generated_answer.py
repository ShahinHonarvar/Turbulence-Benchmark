
def all_left_right_truncatable_prime(nums):
    x = nums[61]
    left_and_right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_left_and_right_truncatable_prime(i):
            left_and_right_truncatable_primes.append(i)
    return sorted(left_and_right_truncatable_primes)
