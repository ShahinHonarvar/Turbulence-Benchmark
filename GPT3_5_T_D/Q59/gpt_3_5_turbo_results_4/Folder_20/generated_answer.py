
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for i in range(10, x):
        if all(is_prime(int(str(i)[j:])) for j in range(len(str(i)))):
            primes.append(i)
    return sorted(primes, reverse=True)
