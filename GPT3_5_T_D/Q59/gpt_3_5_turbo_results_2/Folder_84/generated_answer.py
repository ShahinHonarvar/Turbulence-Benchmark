
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def all_left_truncatable_prime(numbers):
    x = numbers[630]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            is_truncatable = True
            truncated = str(i)
            while is_truncatable and len(truncated) > 1:
                truncated = truncated[1:]
                if not is_prime(int(truncated)):
                    is_truncatable = False
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
