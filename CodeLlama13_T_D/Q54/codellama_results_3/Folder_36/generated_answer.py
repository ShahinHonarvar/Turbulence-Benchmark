
def all_right_truncatable_prime(nums):
    x = nums[992]
    primes = []
    for i in range(x):
        if is_prime(i) and is_truncatable_prime(str(i)):
            primes.append(i)
    return sorted(primes)
