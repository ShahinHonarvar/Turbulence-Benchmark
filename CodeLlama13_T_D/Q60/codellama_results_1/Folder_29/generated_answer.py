
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_right_truncatable_prime(number):
    if number < 10:
        return False
    for i in range(len(str(number)) - 1):
        prefix = str(number)[:i + 1]
        suffix = str(number)[-i - 1:]
        if not is_prime(int(prefix)) or not is_prime(int(suffix)):
            return False
    return True

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
