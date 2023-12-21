
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[69]
    left_truncatable_primes = []
    for i in range(2, x):
        if i == 2 or i == 3 or i == 5 or i == 7:
            left_truncatable_primes.append(i)
        elif '0' not in str(i):
            truncated = str(i)
            while len(truncated) > 1:
                truncated = truncated[1:]
                if not is_prime(int(truncated)):
                    break
            else:
                left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes, reverse=True)
