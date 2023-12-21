
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for number in numbers:
        if is_left_and_right_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(1, int(len(str(n)) / 2) + 1):
        if not is_prime(n):
            return False
        n = int(str(n)[i:] + str(n)[:-i])
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
