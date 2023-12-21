
def all_left_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_prime(number) and contains_no_0(number) and left_and_right_truncatable(number):
            primes.append(number)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n == 2:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def contains_no_0(n):
    while n > 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def left_and_right_truncatable(n):
    while len(str(n)) > 2:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True
