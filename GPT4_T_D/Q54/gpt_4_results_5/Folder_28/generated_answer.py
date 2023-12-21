
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:len(str(n)) - i])):
                return False
        return True

    limit = tup[19]
    right_truncatable_primes = [i for i in range(limit) if is_right_truncatable(i)]
    
    return sorted(right_truncatable_primes)
