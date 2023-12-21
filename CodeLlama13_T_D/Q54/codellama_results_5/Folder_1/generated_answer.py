
def all_right_truncatable_prime(nums):
    x = nums[20]
    right_truncatable_primes = []
    for i in range(x-1, 1, -1):
        if is_prime(i) and is_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[:-i])):
            return False
    return True
