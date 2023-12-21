
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[42]
    right_truncatable_primes = []

    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            digits = str(num)
            for i in range(1, len(digits)):
                truncated_num = int(digits[:-i])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes)
