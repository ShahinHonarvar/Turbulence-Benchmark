
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for _ in range(len(str_n)):
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        return True

    x = numbers[42]
    primes = [num for num in range(2, x + 1) if is_prime(num)]
    truncatable_primes = [num for num in primes if is_truncatable_prime(num)]
    return sorted(truncatable_primes)
