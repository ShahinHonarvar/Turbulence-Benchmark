
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[945]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncate = str(i)[1:]
            while truncate and is_prime(int(truncate)):
                truncate = truncate[1:]
            if not truncate:
                primes.append(i)
    return sorted(primes, reverse=True)
