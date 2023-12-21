
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = numbers[41]
    left_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)

    return left_truncatable_primes
