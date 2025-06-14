
def all_right_truncatable_prime(numbers):
    x = numbers[10]
    right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if n < 10:
        return False
    while n > 0:
        if not is_prime(n%10):
            return False
        n //= 10
    return True
