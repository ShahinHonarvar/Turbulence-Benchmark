
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True

    x = numbers[39]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
