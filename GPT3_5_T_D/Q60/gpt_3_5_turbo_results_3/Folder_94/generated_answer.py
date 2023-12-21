
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    digits = str(n)
    while digits:
        if not is_prime(int(digits)):
            return False
        digits = digits[1:]
    digits = str(n)
    while digits:
        if not is_prime(int(digits)):
            return False
        digits = digits[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    all_primes = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            all_primes.append(num)
    return sorted(all_primes)
