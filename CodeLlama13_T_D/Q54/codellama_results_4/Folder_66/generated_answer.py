
def all_right_truncatable_prime(numbers):
    x = numbers[25]
    primes = []
    for i in range(10**(x-1), 10**x):
        if is_right_truncatable_prime(i, numbers):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_right_truncatable_prime(n, numbers):
    for i in range(len(numbers)):
        if not n % numbers[i]:
            return False
    return True
