
def all_left_truncatable_prime(nums):
    x = nums[30]
    primes = []
    for i in range(1, x+1):
        if is_prime(i) and '0' not in str(i):
            primes.append(i)
    return sorted(primes, reverse=True)
