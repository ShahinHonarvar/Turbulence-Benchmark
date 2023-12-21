
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    s = str(n)
    lens = len(s)
    for i in range(lens):
        left, right = int(s[:i]), int(s[i:])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True
