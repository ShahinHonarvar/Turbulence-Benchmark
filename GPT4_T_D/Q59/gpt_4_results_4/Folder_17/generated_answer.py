
def all_left_truncatable_prime(t):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(0, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    x = t[36]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes, reverse=True)
