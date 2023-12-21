
def all_right_truncatable_prime(numbers):
    x = numbers[88]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable_prime(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)
