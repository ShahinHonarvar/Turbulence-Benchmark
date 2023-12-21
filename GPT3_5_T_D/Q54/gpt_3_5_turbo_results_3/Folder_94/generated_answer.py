
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(num):
    primes = []
    if is_prime(num):
        primes.append(num)
        for i in range(1, len(str(num))):
            if is_prime(int(str(num)[:-i])):
                primes.extend(right_truncatable_prime(int(str(num)[:-i])))
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[43]
    res = []
    for num in range(2, x):
        if num < 10 or num % 10 in (2, 3, 5, 7):
            primes = right_truncatable_prime(num)
            if len(primes) > 0 and primes[-1] < x:
                res.extend(primes)
    return sorted(res)
