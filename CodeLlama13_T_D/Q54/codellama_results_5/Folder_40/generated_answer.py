
def all_right_truncatable_prime(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number) and is_truncatable_prime(number):
            prime_numbers.append(number)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True
