
def all_right_truncatable_prime(numbers):
    x = numbers[73]
    primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    while num > 10:
        num //= 10
        if not is_prime(num):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
