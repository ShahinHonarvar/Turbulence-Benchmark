
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        string_n = str(n)
        if '0' in string_n:
            return False
        for i in range(len(string_n)):
            left_truncated = int(string_n[i:])
            right_truncated = int(string_n[:len(string_n) - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True

    x = numbers[49]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
