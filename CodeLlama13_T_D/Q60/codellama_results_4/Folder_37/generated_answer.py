
def all_left_right_truncatable_prime(nums):
    left_right_primes = []
    for num in nums:
        if is_prime(num) and not contains_zero(str(num)):
            left_right_primes.append(num)
    return sorted(left_right_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
