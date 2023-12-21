
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    x = numbers[86]
    for i in range(2, x):
        if '0' not in str(i):
            truncated = str(i)
            while len(truncated) > 1:
                truncated = truncated[1:]
                if not is_prime(int(truncated)):
                    break
            else:
                primes.append(i)

    return sorted(primes, reverse=True)
