
def all_left_right_truncatable_prime(nums):
    x = nums[175]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if int(s[i:]) % 2 == 0 or int(s[:-i]) % 2 == 0:
            return False
    return True
