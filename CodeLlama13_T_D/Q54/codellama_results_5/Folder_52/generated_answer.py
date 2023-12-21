
def all_right_truncatable_prime(nums):
    x = nums[52]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True
