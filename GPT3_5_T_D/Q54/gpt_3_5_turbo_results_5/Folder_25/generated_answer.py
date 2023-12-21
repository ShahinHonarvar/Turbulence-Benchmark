
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[92]
    right_truncatable_primes = []

    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[:-i])): # remove rightmost digit one by one
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes)
