
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        digits = list(str(n))
        for i in range(1, len(digits)):
            if not is_prime(int(''.join(digits[i:]))):
                return False
            if not is_prime(int(''.join(digits[:i]))):
                return False
        return True

    x = numbers[94]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes)
