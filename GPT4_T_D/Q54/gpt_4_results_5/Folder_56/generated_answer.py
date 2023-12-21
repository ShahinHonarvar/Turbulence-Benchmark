
def all_right_truncatable_prime(numbers):
    x = numbers[30]
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(y):
        while y > 0:
            if not is_prime(y):
                return False
            y //= 10
        return True

    all_right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            all_right_truncatable_primes.append(i)
            
    return sorted(all_right_truncatable_primes)
