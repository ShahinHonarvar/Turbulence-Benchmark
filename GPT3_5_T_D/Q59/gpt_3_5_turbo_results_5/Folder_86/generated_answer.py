
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    truncatable_primes = []

    for x in range(numbers[126] - 1, 1, -1):
        if '0' not in str(x):
            is_truncatable = True
            while is_truncatable and x > 0:
                if not is_prime(x):
                    is_truncatable = False
                x //= 10
            if is_truncatable:
                truncatable_primes.append(x)

    truncatable_primes.sort(reverse=True)
    return truncatable_primes
