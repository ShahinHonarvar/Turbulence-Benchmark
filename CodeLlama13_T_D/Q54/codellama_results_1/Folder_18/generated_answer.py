
def all_right_truncatable_prime(numbers):
    x = numbers[429]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
