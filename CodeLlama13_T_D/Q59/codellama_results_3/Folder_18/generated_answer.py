
def all_left_truncatable_prime(numbers):
    x = numbers[429]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and not contains_0(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_0(s):
    return '0' in s
