
def all_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            primes.append(number)
    return sorted(primes)

def is_right_truncatable_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
