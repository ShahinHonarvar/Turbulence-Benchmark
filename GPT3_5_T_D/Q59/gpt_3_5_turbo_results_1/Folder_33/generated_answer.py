
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[945]
    truncatable_primes = []

    for num in range(x-1, 1, -1):
        if all(digit != '0' and is_prime(int(str(num)[:i])) for i, digit in enumerate(str(num), start=1)):
            truncatable_primes.append(num)

    return truncatable_primes
