
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_digits = len(str(n))
        for i in range(num_digits):
            truncated_num = int(str(n)[i:])
            if not is_prime(truncated_num):
                return False
        return True

    x = numbers[760]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
