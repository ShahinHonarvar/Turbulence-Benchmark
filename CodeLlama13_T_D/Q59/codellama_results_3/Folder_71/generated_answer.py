
def all_left_truncatable_prime(nums):
    x = nums[22]
    primes = []
    for i in range(10**x-1, 10**x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(n):
    if n < 2 or any(int(n % 10**k) == 0 for k in range(1, len(str(n)))):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(n % 10**i)):
            return False
    return True

def is_prime(n):
    if n < 2 or any(n % k == 0 for k in range(2, int(n ** 0.5) + 1)):
        return False
    return True
