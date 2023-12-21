
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    while n > 9:
        if not is_prime(n):
            return False
        n //= 10
    return True

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
