
def all_left_truncatable_prime(numbers):
    x = numbers[6]
    prime_numbers = []
    for i in range(10**(x-1), 10**x):
        if is_left_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_left_truncatable_prime(n):
    if n % 10 == 0 or not is_prime(n):
        return False
    for i in range(1, int(len(str(n))/2)):
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
