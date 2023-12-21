
def all_left_right_truncatable_prime(numbers):
    x = numbers[370]
    primes = []
    for i in range(x):
        if is_prime(i) and is_left_and_right_truncatable(i, x):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n, x):
    if '0' in str(n):
        return False
    for i in range(2, int(x**0.5) + 1):
        if n % i == 0:
            return False
    return True
