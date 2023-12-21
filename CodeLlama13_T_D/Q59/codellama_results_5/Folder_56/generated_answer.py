
def all_left_truncatable_prime(nums):
    primes = []
    for i in range(len(nums)):
        num = nums[i]
        if is_prime(num) and not contains_zero(num):
            primes.append(num)
    return primes

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(n):
    while n > 0:
        if n % 10 == 0:
            return True
        n //= 10
    return False
