
def all_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(1, int(str(num)[::-1])+1):
        if not is_prime(num % (10**i)):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
