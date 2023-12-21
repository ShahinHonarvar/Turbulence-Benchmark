
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[64]
    right_truncatable_primes = []
    for num in range(1, x):
        if is_prime(num):
            num_str = str(num)
            is_right_truncatable_prime = True
            for i in range(1, len(num_str)):
                truncated_num = int(num_str[:-i])
                if not is_prime(truncated_num):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
