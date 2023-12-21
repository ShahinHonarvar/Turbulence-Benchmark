
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    primes = []
    if is_prime(n):
        primes.append(n)
    for i in range(1, 10):
        next_num = n * 10 + i
        if is_prime(next_num):
            primes.extend(right_truncatable_prime(next_num))
    return primes

def all_right_truncatable_prime(nums):
    x = nums[97]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable_primes.extend(right_truncatable_prime(i))
    return sorted(right_truncatable_primes)
