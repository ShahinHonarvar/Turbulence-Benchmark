
def all_left_right_truncatable_prime(nums):
    x = nums[86]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            if left_right_truncatable_prime(i, str(i)):
                primes.append(i)
    return sorted(primes)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s

def left_right_truncatable_prime(n, s):
    while len(s) > 1:
        if not is_prime(int(s)):
            return False
        s = s[1:-1]
    return True
