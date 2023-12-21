
def all_right_truncatable_prime(t):
    x = t[975]
    if x == 0:
        return []
    def check_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def right_truncatable_prime(n):
        while n != 0:
            if not check_prime(n):
                return False
            n = n // 10
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
