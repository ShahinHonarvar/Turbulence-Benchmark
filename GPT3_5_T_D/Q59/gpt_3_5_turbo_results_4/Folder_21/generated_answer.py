
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[175]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncated = str(i)
            while truncated:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[1:]
            else:
                primes.append(i)
    return sorted(primes)
