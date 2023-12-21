
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[94]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                truncatable = False
                break
        if truncatable:
            left_truncatable_primes.append(num)

    return sorted(left_truncatable_primes)
