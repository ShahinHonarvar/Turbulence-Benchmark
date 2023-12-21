
def all_right_truncatable_prime(nums):
    x = nums[88]
    right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and all(is_prime(i//10**j) for j in range(1, len(str(i))-1)):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
