
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True
