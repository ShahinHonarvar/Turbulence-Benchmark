
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if str(num).count('0') == 0 and is_prime(num) and left_truncatable(num):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True
