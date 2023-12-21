
def all_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_right_truncatable_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and is_prime(num/i):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
