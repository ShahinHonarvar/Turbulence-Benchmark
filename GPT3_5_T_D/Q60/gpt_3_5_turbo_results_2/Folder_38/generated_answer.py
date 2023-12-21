
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if "0" in str(n):
            return False

        digits = len(str(n))
        while digits > 1:
            n = int(str(n)[1:])

            if not is_prime(n):
                return False

            n = int(str(n)[:-1])
            digits -= 1

        return is_prime(n)

    x = numbers[28]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]

    return truncatable_primes
