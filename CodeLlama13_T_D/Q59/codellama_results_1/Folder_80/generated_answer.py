
def all_left_truncatable_prime(numbers):
    x = numbers[14]
    left_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
