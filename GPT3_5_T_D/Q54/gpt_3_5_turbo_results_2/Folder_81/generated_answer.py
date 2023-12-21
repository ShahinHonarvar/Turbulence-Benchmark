
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[98]
    primes = []
    for i in range(2, x):
        num = str(i)
        if is_prime(i):
            while len(num) > 0:
                if not is_prime(int(num)):
                    break
                num = num[:-1]
            if len(num) == 0:
                primes.append(i)
    return sorted(primes)
