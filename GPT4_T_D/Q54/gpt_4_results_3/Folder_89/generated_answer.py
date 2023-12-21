
def all_right_truncatable_prime(tup):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num > 0:
            num //= 10
            if num > 0 and not is_prime(num):
                return False
        return True

    x = tup[97]
    truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
