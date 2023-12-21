
def all_right_truncatable_prime(tuple):
    x = tuple[49]
    prime_numbers = []
    for i in range(2, x):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, key=lambda x: x)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
