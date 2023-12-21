
def all_left_truncatable_prime(tuple):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def left_truncated_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    x = tuple[758]
    left_truncatable_primes = []
    for i in range(1, x):
        if left_truncated_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
