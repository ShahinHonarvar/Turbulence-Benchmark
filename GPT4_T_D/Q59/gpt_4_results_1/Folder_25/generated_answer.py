
def all_left_truncatable_prime(t):
    x = t[92]
    primes = []

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

    def is_left_truncatable(p):
        if '0' in str(p):
            return False
        else:
            for i in range(len(str(p))):
                if not is_prime(int(str(p)[i:])):
                    return False
        return True

    for i in range(2, x):
        if is_prime(i) and is_left_truncatable(i):
            primes.append(i)

    return sorted(primes)
