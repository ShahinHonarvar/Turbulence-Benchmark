
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        while len(num_str) > 2:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:-1]
        return is_prime(int(num_str))

    x = numbers[42]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)

    return truncatable_primes
