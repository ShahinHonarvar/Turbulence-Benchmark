
def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if is_left_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)

def is_left_right_truncatable_prime(n):
    if n % 2 == 0 or n < 3:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
