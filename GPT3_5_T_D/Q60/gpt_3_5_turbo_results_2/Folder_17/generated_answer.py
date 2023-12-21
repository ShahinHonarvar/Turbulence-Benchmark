
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        while len(num_str) > 2:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True

    x = numbers[36]
    truncatable_primes = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
