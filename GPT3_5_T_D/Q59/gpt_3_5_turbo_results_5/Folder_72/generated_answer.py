
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[31]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            truncate = str(i)
            while truncate:
                if not is_prime(int(truncate)):
                    break
                truncate = truncate[1:]
            else:
                primes.append(i)
    return sorted(primes, reverse=True)
