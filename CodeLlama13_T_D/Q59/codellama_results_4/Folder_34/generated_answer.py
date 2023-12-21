
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(n):
    if n < 2 or any(int(str(n)[i]) == 0 for i in range(1, len(str(n)) - 1)):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def is_prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        return False
    return True
