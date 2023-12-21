
def all_right_truncatable_prime(numbers):
    x = numbers[31]
    primes = []
    for num in range(x):
        if is_right_truncatable_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_right_truncatable_prime(num):
    if num < 2:
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
