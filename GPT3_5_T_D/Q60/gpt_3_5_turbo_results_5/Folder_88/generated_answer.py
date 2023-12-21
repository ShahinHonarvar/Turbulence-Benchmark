
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            n_str = n_str[1:]
            if not is_prime(int(n_str)):
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            n_str = n_str[:-1]
            if not is_prime(int(n_str)):
                return False
        return True

    x = numbers[93]
    left_right_truncatable_primes = []
    for i in range(2, x+1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes
