
def all_left_right_truncatable_prime(nums):
    x = nums[26]
    primes = []
    for i in range(x):
        if is_prime(i) and not '0' in str(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
