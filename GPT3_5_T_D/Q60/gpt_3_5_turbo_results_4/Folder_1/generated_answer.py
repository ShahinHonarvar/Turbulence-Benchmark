
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i])):
                return False
        return True

    x = numbers[20]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
