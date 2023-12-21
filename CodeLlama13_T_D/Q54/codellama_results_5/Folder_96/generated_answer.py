
def all_right_truncatable_prime(nums):
    x = nums[29]
    primes = []
    for i in range(10, x+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
