
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        while num >= 10:
            if not is_prime(num):
                return False
            num //= 10
        return is_prime(num)

    x = numbers[24]

    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes)
