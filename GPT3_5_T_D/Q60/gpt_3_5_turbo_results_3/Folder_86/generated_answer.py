
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 10:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)

    x = numbers[126]
    primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)
