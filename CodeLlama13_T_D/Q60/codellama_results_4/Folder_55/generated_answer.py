
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Invalid argument")
    for i in range(len(str(n))):
        num = int(str(n)[i:] + str(n)[:i])
        if not is_prime(num):
            return False
    return True
