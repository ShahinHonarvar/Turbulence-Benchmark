
def all_left_right_truncatable_prime(nums):
    x = nums[8]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(2, x+1):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(set(left_truncatable_primes + right_truncatable_primes), reverse=True)

def is_left_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
