
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x >= 23:
            for i in range(2, x):
                if '0' in str(i):
                    continue
                truncated = str(i)
                if not is_prime(int(truncated)):
                    continue
                while len(truncated) > 1:
                    truncated = truncated[1:-1]
                    if not is_prime(int(truncated)):
                        break
                else:
                    primes.append(i)
    return sorted(primes)
