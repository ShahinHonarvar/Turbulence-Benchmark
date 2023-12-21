
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
