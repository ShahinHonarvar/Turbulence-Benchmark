
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for n in range(2, x + 1):
        if '0' not in str(n):
            if is_prime(n):
                truncated = str(n)
                while len(truncated) > 2:
                    truncated = truncated[1:-1]
                    if not is_prime(int(truncated)):
                        break
                if len(truncated) <= 2:
                    primes.append(n)
    return sorted(primes, reverse=True)
