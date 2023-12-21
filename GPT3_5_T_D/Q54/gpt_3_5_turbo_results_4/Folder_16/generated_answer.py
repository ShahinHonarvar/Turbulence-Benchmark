
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[792]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            num = i
            while num > 0:
                if not is_prime(num):
                    truncatable = False
                    break
                num //= 10
            if truncatable:
                truncatable_primes.append(i)

    return sorted(truncatable_primes)
