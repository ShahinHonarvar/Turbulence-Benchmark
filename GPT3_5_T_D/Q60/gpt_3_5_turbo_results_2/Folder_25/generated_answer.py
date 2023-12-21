
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        digits = str(n)
        while digits:
            if not is_prime(int(digits)):
                return False
            digits = digits[1:]
        digits = str(n)
        while digits:
            if not is_prime(int(digits)):
                return False
            digits = digits[:-1]
        return True

    x = numbers[92]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
