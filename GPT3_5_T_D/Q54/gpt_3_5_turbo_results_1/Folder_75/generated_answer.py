
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[41]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_num = num
            is_right_truncatable_prime = True
            while truncated_num > 10:
                truncated_num //= 10
                if not is_prime(truncated_num):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
