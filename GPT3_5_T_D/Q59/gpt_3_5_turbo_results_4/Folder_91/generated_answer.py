
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[0]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            is_left_truncatable = all(is_prime(int(str(i)[j:])) for j in range(len(str(i))))
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
