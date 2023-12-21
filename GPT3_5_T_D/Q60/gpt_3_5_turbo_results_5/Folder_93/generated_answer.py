
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        digits = str(n)
        if '0' in digits:
            return False

        for i in range(len(digits)):
            if not is_prime(int(digits[i:])):
                return False
            if not is_prime(int(digits[:i+1])):
                return False
        return True

    primes = [n for n in numbers if is_truncatable_prime(n)]
    return sorted(primes)
