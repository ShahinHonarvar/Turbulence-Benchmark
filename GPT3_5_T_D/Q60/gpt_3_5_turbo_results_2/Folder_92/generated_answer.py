
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
            if not is_prime(int(n_str[:i + 1])):
                return False
        return True

    x = numbers[7]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
