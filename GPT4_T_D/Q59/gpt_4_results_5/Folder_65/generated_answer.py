
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(0, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True


def all_left_truncatable_prime(nums):
    x = nums[32]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
