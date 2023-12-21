
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[784]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            is_truncatable = True
            for j in range(len(str(i))):
                truncated = int(str(i)[j:])
                if not is_prime(truncated):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)
