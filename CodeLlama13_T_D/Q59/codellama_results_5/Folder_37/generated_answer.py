
def all_left_truncatable_prime(nums):
    x = nums[35]
    primes = []
    for i in range(x+1, 0, -1):
        if is_prime(i) and '0' not in str(i):
            primes.append(i)
    return sorted(primes, reverse=True)
