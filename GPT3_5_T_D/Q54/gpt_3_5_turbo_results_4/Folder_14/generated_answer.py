
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_right(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(numbers):
    x = numbers[78]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated = truncate_right(num)
            while truncated >= 2:
                if not is_prime(truncated):
                    break
                truncated = truncate_right(truncated)
            if truncated < 2:
                primes.append(num)
    return sorted(primes, reverse=True)
