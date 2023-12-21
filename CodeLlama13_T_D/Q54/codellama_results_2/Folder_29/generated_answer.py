
def all_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for i in range(10**4, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while len(str(n)) > 1:
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True
