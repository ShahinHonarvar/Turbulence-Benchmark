
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(numbers):
    x = numbers[19]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        if is_prime(i):
            truncated = str(i)
            while truncated != '':
                truncated = truncated[1:]
                if not is_prime(int(truncated)):
                    break
            else:
                left_truncatable_primes.append(i)
    return left_truncatable_primes
