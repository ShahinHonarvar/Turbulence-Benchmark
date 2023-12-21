
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[67]
    truncatable_primes = []
    for i in range(2, x):
        num = str(i)
        while len(num) > 0 and is_prime(int(num)):
            num = num[:-1]
        if len(num) == 0:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
