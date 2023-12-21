
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    return truncatable_prime(int(str(n)[1:])) and truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if truncatable_prime(num):
            primes.append(num)
    primes.sort()
    return primes
