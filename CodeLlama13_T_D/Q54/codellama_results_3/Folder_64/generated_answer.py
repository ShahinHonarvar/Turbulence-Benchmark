
def all_right_truncatable_prime(nums):
    x = nums[4]
    primes = []
    for i in range(x+1):
        if is_prime(i) and is_right_truncatable_prime(str(i)):
            primes.append(i)
    return sorted(primes)
