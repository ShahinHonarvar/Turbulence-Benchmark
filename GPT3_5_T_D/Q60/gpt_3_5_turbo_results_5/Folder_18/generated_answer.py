
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
            if not is_prime(int(n_str[:i+1])):
                return False
        return True

    x = numbers[429]
    truncatable_primes = []
    for i in range(x, 1, -1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
