
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            for j in range(len(str(i))):
                truncatable = truncatable and is_prime(int(str(i)[j:]))
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
