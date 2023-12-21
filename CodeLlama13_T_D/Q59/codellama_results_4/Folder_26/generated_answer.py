
def all_left_truncatable_prime(nums):
    x = nums[81]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)
