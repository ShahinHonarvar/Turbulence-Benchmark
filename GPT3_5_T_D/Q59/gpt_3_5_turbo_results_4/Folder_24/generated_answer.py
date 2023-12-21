
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[65]
    primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncatable = True
        while truncatable and i > 10:
            i = int(str(i)[1:])
            if not is_prime(i):
                truncatable = False
        if truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)
