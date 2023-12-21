
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_left_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            truncatable = True
            for j in range(1, len(num)):
                truncated = int(num[j:])
                if not is_prime(truncated):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return primes
