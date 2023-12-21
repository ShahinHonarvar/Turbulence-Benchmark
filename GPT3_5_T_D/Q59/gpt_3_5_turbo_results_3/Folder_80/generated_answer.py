
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for n in range(2, x):
        if '0' not in str(n):
            truncatable = True
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[i:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(n)
    return sorted(primes, reverse=True)
